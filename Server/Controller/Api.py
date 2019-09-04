import json
import Server
import socket
import struct
import time
import urllib.parse
import requests
import sys
import string

rootPath = '.'

try:
	from PIL import Image
except ImportError:
	import Image
import Server
import os

def success(request, response, s):
	response.write(json.dumps({'success': True, 'result': s}))

def error(request, response, s):
	response.write(json.dumps({'success': False, 'result': s}))

def getUser(request, response):
	response.write(json.dumps(request.user.__dict__))

def getSearch(request, response):
	response.write(json.dumps([]))

def getTitles(request, response):
	response.write(json.dumps([]))


def serveFile(response, path, filename = None, start = None, end = None):
	try:
		if start is not None:
			start = int(start)

		if end is not None:
			end = int(end)

		if not filename:
			filename = os.path.basename(path)

		response.attachFile(filename)
	
		chunkSize = 0x400000

		with open(path, "rb") as f:
			f.seek(0, 2)
			size = f.tell()
			if start and end:
				if end == None:
					end = size - 1
				else:
					end = int(end)

				if start == None:
					start = size - end
				else:
					start = int(start)

				if start >= size or start < 0 or end <= 0:
					return Server.Response400(request, response, 'Invalid range request %d - %d' % (start, end))

				response.setStatus(206)

			else:
				if start == None:
					start = 0
				if end == None:
					end = size

			if end >= size:
				end = size

				if end <= start:
					response.write(b'')
					return

			print('ranged request for %d - %d' % (start, end))
			f.seek(start, 0)

			response.setMime(path)
			response.setHeader('Accept-Ranges', 'bytes')
			response.setHeader('Content-Range', 'bytes %s-%s/%s' % (start, end-1, size))
			response.setHeader('Content-Length', str(end - start))
			response.sendHeader()

			if not response.head:
				size = end - start

				i = 0
				#status = Status.create(size, 'Downloading ' + os.path.basename(path))

				while i < size:
					chunk = f.read(min(size-i, chunkSize))
					i += len(chunk)

					#status.add(len(chunk))

					if chunk:
						pass
						response.write(chunk)
					else:
						break
				#status.close()
	except BaseException as e:
		print('File download exception: ' + str(e))

	if response.bytesSent == 0:
		response.write(b'')

def  isWindows():
	if "win" in sys.platform[:3].lower():
		return True
	else:
		return False

def listDrives():
	drives = []
	if isWindows():
		import string
		import ctypes
		kernel32 = ctypes.windll.kernel32
		bitmask = kernel32.GetLogicalDrives()
		for letter in string.ascii_uppercase:
			if bitmask & 1:
				drives.append(letter)
			bitmask >>= 1
		return drives
	else:
		return ['root'];

def isBlocked(path):
	path = path.lower()

	whitelist = ['.nro', '.xci', '.nsp', '.conf', '.json', '.db', '.tfl', '.jpg', '.gif', '.png', '.bin', '.enc', '.ini', '.ips', '.txt']

	for ext in whitelist:
		if path.endswith(ext):
			return False

	return True

def cleanPath(path = None):
	if not path:
		return None
	bits = path.replace('\\', '/').split('/')
	drive = bits[0]
	bits = bits[1:]

	if isWindows():
		path = os.path.abspath(os.path.join(drive+':/', '/'.join(bits)))
	else:
		path = os.path.abspath('/'.join(bits))

	#if not path.startswith(os.path.abspath(rootPath)):
	#	raise IOError('invalid path requested: ' + path)
	return path

def getDirectoryList(request, response):
	r = {'dirs': [], 'files': []}
	try:
		path = ''
		for i in request.bits[2:]:
			path = os.path.join(path, i)

		if path:
			path = cleanPath(path)

		r = {'dirs': [], 'files': []}

		if not path:
			for d in listDrives():
				r['dirs'].append({'name': d})
			response.write(json.dumps(r))
			return
	
		for name in os.listdir(path):
			abspath = os.path.join(path, name)

			if os.path.isdir(abspath):
				r['dirs'].append({'name': name})
			elif os.path.isfile(abspath):
				if not isBlocked(abspath):
					r['files'].append({'name': name, 'size': os.path.getsize(abspath), 'mtime': os.path.getmtime(abspath)})
	except:
		raise
		raise IOError('dir list access denied')
	response.write(json.dumps(r))

def getFile(request, response, start = None, end = None):
	path = ''
	for i in request.bits[2:]:
		path = os.path.join(path, i)
	path = cleanPath(path)

	if isBlocked(path):
		raise IOError('read access denied')

	if 'Range' in request.headers:
		start, end = request.headers.get('Range').strip().strip('bytes=').split('-')

		if end != '':
			end = int(end) + 1

		if start != '':
			start = int(start)

	return serveFile(response, path, start = start, end = end)

def getFileSize(request, response):
	t = {}
	path = ''
	for i in request.bits[2:]:
		path = os.path.join(path, i)
	path = cleanPath(path)
	try:
		t['size'] = os.path.getsize(path);
		t['mtime'] = os.path.getmtime(path);
		response.write(json.dumps(t))
	except BaseException as e:
		response.write(json.dumps({'success': False, 'message': str(e)}))


