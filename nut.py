import usb.core
import usb.util
import struct
import sys
from binascii import hexlify as hx, unhexlify as uhx
from pathlib import Path
import Server
import Server.Controller.Api
import time
from urllib.parse import urlparse
from urllib.parse import parse_qs
import Server.Controller.Api
import threading

global status
status = 'initializing'

def getFiles():
	for k, t in Titles.items():
		f = t.getLatestFile()
		if f and f.hasValidTicket:
			o.append({'id': t.id, 'name': t.name, 'version': int(f.version) if f.version else None , 'size': f.getFileSize(), 'mtime': f.getFileModified() })

	return json.dumps(o)

class UsbResponse(Server.NutResponse):
	def __init__(self, packet):
		super(UsbResponse, self).__init__(None)
		self.packet = packet

	def sendHeader(self):
		pass

	def write(self, data):
		print('usbresponse write')
		if self.bytesSent == 0 and not self.headersSent:
			self.sendHeader()

		if type(data) == str:
			data = data.encode('utf-8')

		self.bytesSent += len(data)
		self.packet.payload = data
		self.packet.send()

		self.bytesSent += len(data)


class UsbRequest(Server.NutRequest):
	def __init__(self, url):
		self.headers = {}
		self.path = url
		self.head = False
		self.url = urlparse(self.path)

		print('url ' + self.path);

		self.bits = [x for x in self.url.path.split('/') if x]
		print(self.bits)
		self.query = parse_qs(self.url.query)

		try:
			for k,v in self.query.items():
				self.query[k] = v[0];
		except:
			pass

		self.user = None

class Packet:
	def __init__(self, i, o):
		self.size = 0
		self.payload = b''
		self.command = 0
		self.threadId = 0
		self.packetIndex = 0
		self.packetCount = 0
		self.timestamp = 0
		self.i = i
		self.o = o
		
	def recv(self, timeout = 60000):
		print('begin recv')
		header = bytes(self.i.read(32, timeout=timeout))
		print('read complete')
		magic = header[:4]
		self.command = int.from_bytes(header[4:8], byteorder='little')
		self.size = int.from_bytes(header[8:16], byteorder='little')
		self.threadId = int.from_bytes(header[16:20], byteorder='little')
		self.packetIndex = int.from_bytes(header[20:22], byteorder='little')
		self.packetCount = int.from_bytes(header[22:24], byteorder='little')
		self.timestamp = int.from_bytes(header[24:32], byteorder='little')
		
		if magic != b'\x12\x12\x12\x12':
			print('invalid magic! ' + str(magic));
			return False
		
		print('receiving %d bytes' % self.size)
		self.payload = bytes(self.i.read(self.size, timeout=0))
		return True
		
	def send(self, timeout = 60000):
		print('sending %d bytes' % len(self.payload))
		self.o.write(b'\x12\x12\x12\x12', timeout=timeout)
		self.o.write(struct.pack('<I', self.command), timeout=timeout)
		self.o.write(struct.pack('<Q', len(self.payload)), timeout=timeout) # size
		self.o.write(struct.pack('<I', 0), timeout=timeout) # threadId
		self.o.write(struct.pack('<H', 0), timeout=timeout) # packetIndex
		self.o.write(struct.pack('<H', 0), timeout=timeout) # packetCount
		self.o.write(struct.pack('<Q', 0), timeout=timeout) # timestamp
		self.o.write(self.payload, timeout=timeout)

class Usb:
	def __init__(self, ctx):
		self.ctx = ctx

	def init(self):

		p = Packet(self.ctx.global_in, self.ctx.global_out)
		while True:
			if p.recv(0):
				if p.command == 1:
					print('Recv command! %d' % p.command)
					req = UsbRequest(p.payload.decode('utf-8'))
					resp = UsbResponse(p)

					Server.route(req, resp)
				else:
					print('Unknown command! %d' % p.command)
			else:
				print('failed to read!')

def startNetwork(ctx):
	thread = threading.Thread(target=Server.run, args=(ctx,))
	thread.daemon = True
	thread.start()