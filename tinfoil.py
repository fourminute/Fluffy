import socket
import random

try:
    from SimpleHTTPServer import SimpleHTTPRequestHandler
    from SocketServer import TCPServer
    from urllib import quote
except ImportError:
    from http.server import SimpleHTTPRequestHandler
    from socketserver import TCPServer
    from urllib.parse import quote

# Tinfoil Network
netrlist = []
def reset_netrlist():
    global netrlist
    netrlist = None
    netrlist = []
def append_netrlist(v, v2):
    global netrlist
    netrlist.append((v, v2))

class Network:
    def __init__(self, ctx):
        self.ctx = ctx

    def init(self):
        reset_netrlist()
        accepted_extension = ('.nsp')
        hostPort = random.randint(26490,26999)
        target_ip = self.ctx.switch_ip
        hostIp = self.ctx.host_ip
        target_path = str(selected_dir).strip()
        baseUrl = hostIp + ':' + str(hostPort) + '/'
        directory = target_path
        file_list_payload = ''  
        for file in [file for file in next(os.walk(target_path))[2] if file.endswith(accepted_extension)]:
            for y in selected_files:
                if str(file).find(os.path.basename(y)) != -1:
                    n = random.randint(1,10000000)
                    fake_file = str(n) + ".nsp"
                    append_netrlist(fake_file, str(y))
                    file_list_payload += baseUrl + fake_file + '\n'
        file_list_payloadBytes = file_list_payload.encode('ascii')
        if directory and directory != '.':
            os.chdir(directory)
        server = TinfoilServer((host_ip, hostPort), TinfoilHTTPHandler)
        thread = threading.Thread(target=server.serve_forever)
        thread.daemon = True
        thread.start()
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((target_ip, 2000))
            sock.sendall(struct.pack('!L', len(file_list_payloadBytes)) + file_list_payloadBytes)
            while len(sock.recv(1)) < 1:
                if task_canceled:
                    server.force_stop()
                    sys.exit()
                time.sleep(0.1)
            sock.close()
        except Exception as e:
            if is_logging:
                logging.error(e, exc_info=True)
            server.force_stop()
            throw_error(1)
            sys.exit()
        complete_install()
        server.force_stop()
        sys.exit()

class TinfoilHTTPHandler(SimpleHTTPRequestHandler):
    def send_head(self):
        for s in range(len(netrlist)):
            if netrlist[s][0] == str(self.path)[1:]:
                path = netrlist[s][1]
        ctype = self.guess_type(path)
        if os.path.isdir(path):
            return SimpleHTTPRequestHandler.send_head(self)
        if not os.path.exists(path):
            return self.send_error(404, self.responses.get(404)[0])
        f = open(path, 'rb')
        fs = os.fstat(f.fileno())
        size = fs[6]
        start, end = 0, size - 1
        if 'Range' in self.headers:
            start, end = self.headers.get('Range').strip().strip('bytes=')\
                .split('-')
        if start == "":
            try:
                end = int(end)
            except ValueError as e:
                self.send_error(400, 'invalid range')
            start = size - end
        else:
            try:
                start = int(start)
            except ValueError as e:
                self.send_error(400, 'invalid range')
            if start >= size:
                self.send_error(416, self.responses.get(416)[0])
            if end == "":
                end = size - 1
            else:
                try:
                    end = int(end)
                except ValueError as e:
                    self.send_error(400, 'invalid range')

        start = max(start, 0)
        end = min(end, size - 1)
        self.range = (start, end)
        cont_length = end - start + 1
        if 'Range' in self.headers:
            self.send_response(206)
        else:
            self.send_response(200)
        self.send_header('Content-type', ctype)
        self.send_header('Accept-Ranges', 'bytes')
        self.send_header('Content-Range','bytes %s-%s/%s' % (start, end, size))
        self.send_header('Content-Length', str(cont_length))
        self.send_header('Last-Modified', self.date_time_string(fs.st_mtime))
        self.end_headers()
        return f

    def copyfile(self, infile, outfile):
        if 'Range' not in self.headers:
            SimpleHTTPRequestHandler.copyfile(self, infile, outfile)
            return
        complete_loading()
        set_cur_nsp(str(os.path.basename(infile.name)))
        start, end = self.range
        infile.seek(start)
        bufsize = 64 * 1024  # 64KB
        while True:
            if task_canceled: sys.exit()
            buf = infile.read(bufsize)
            if not buf:
                break
            try:
                outfile.write(buf)
                try:
                    set_progress(int(infile.tell()), int(end))
                    elapsed_time = time.time() - start_time
                    if elapsed_time >= 1:
                        set_cur_transfer_rate(int(infile.tell()) - last_transfer_rate)
                        set_last_transfer_rate(int(infile.tell()))
                        set_start_time()
                except:
                    pass
            except BrokenPipeError:
                pass    
class TinfoilServer(TCPServer):
    stopped = False
    def server_bind(self):
        import socket
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(self.server_address)
    def serve_forever(self):
        while not self.stopped:
            if task_canceled: sys.exit()
            self.handle_request()
        sys.exit()
    def force_stop(self):
        self.server_close()
        self.stopped = True
        sys.exit()
        
    
# Tinfoil USB
class Usb:
    CMD_ID_EXIT = 0
    CMD_ID_FILE_RANGE = 1
    CMD_TYPE_RESPONSE = 1
    
    def __init__(self, ctx):
        self.ctx = ctx
    
    def init(self):
        try:
            detach_switch()
            connect_switch()
            self.send_nsp_list()
            self.process()
            complete_install()
            sys.exit()
        except Exception as e:
            if is_logging:
                logging.error(e, exc_info=True)
            throw_error(2)
            sys.exit()
        
    def send_response_header(self, cmd_id, data_size):
        global_out.write(b'TUC0')
        global_out.write(struct.pack('<B', self.CMD_TYPE_RESPONSE))
        global_out.write(b'\x00' * 3)
        global_out.write(struct.pack('<I', cmd_id))
        global_out.write(struct.pack('<Q', data_size))
        global_out.write(b'\x00' * 0xC)
        
    def file_range_cmd(self, data_size):
        file_range_header = global_in.read(0x20)
        range_size = struct.unpack('<Q', file_range_header[:8])[0]
        range_offset = struct.unpack('<Q', file_range_header[8:16])[0]
        nsp_name_len = struct.unpack('<Q', file_range_header[16:24])[0]
        nsp_name = bytes(global_in.read(nsp_name_len)).decode('utf-8')
        set_cur_nsp(str(os.path.basename(nsp_name)))
        self.send_response_header(self.CMD_ID_FILE_RANGE, range_size)
        with open(nsp_name, 'rb') as f:
            complete_loading()
            f.seek(range_offset)
            curr_off = 0x0
            end_off = range_size
            read_size = transfer_rate
            while curr_off < end_off:
                if task_canceled: sys.exit()
                if curr_off + read_size >= end_off:
                    read_size = end_off - curr_off
                    try:
                        set_progress(int(end_off), int(end_off))
                    except:
                        pass
                buf = f.read(read_size)
                global_out.write(data=buf, timeout=0)
                curr_off += read_size
                try:
                    set_progress(int(curr_off), int(end_off))
                    elapsed_time = time.time() - start_time
                    if elapsed_time >= 1:
                        set_cur_transfer_rate(curr_off - last_transfer_rate)
                        set_last_transfer_rate(curr_off)
                        set_start_time()
                except:
                    pass
                
    def process(self):
        while True:
            if task_canceled: sys.exit()
            cmd_header = bytes(global_in.read(0x20, timeout=0))
            magic = cmd_header[:4]
            if magic != b'TUC0': 
                continue
            cmd_type = struct.unpack('<B', cmd_header[4:5])[0]
            cmd_id = struct.unpack('<I', cmd_header[8:12])[0]
            data_size = struct.unpack('<Q', cmd_header[12:20])[0]
            if cmd_id == self.CMD_ID_EXIT:
                complete_install()
                sys.exit()
            elif cmd_id == self.CMD_ID_FILE_RANGE:
                self.file_range_cmd(data_size)

    def send_nsp_list(self):
        nsp_path_list = list()
        nsp_path_list_len = 0
        for nsp_path in os.listdir(selected_dir):
            if nsp_path.endswith(".nsp"):
                for y in selected_files:
                    if str(nsp_path).find(os.path.basename(y)) != -1:
                        print(str(nsp_path))
                        nsp_path_list.append(selected_dir + "/" + nsp_path.__str__() + '\n')
                        nsp_path_list_len += len(selected_dir + "/" + nsp_path.__str__()) + 1
        global_out.write(b'TUL0')
        global_out.write(struct.pack('<I', nsp_path_list_len))
        global_out.write(b'\x00' * 0x8) 
        for nsp_path in nsp_path_list:
            global_out.write(nsp_path)