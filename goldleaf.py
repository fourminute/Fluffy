# Goldleaf            
class GoldleafCommandId:
    ListSystemDrives = 0
    GetEnvironmentPaths = 1
    GetPathType = 2
    ListDirectories = 3
    ListFiles = 4
    GetFileSize = 5
    FileRead = 6
    FileWrite = 7
    CreateFile = 8
    CreateDirectory = 9
    DeleteFile = 10
    DeleteDirectory = 11
    RenameFile = 12
    RenameDirectory = 13
    GetDriveTotalSpace = 14
    GetDriveFreeSpace = 15
    GetNSPContents = 16
    Max = 17

class GoldleafCommandReadResult:
    Success = 0
    InvalidMagic = 1
    InvalidGoldleafCommandId = 2

class Goldleaf:
    GLUC         = b"GLUC"
    magic        = b"GLUC"
    cmd_id       = 0
    drives       = {}
    FW_DENIED = 0
    FW_ACCEPTED = 1
    FW_NOSTATUS = 2
    fw_status = FW_NOSTATUS
    
    def __init__(self, ctx):
        self.ctx = ctx
    
    def init(self):
        try:
            detach_switch()
            connect_switch()
            self.process()
        except Exception as e:
            if is_logging:
                logging.error(e, exc_info=True)
            throw_error(0)
            sys.exit()
        
    def write(self,buffer):
        try:
            global_out.write(buffer,timeout=3000)
        except:
            pass

    def read(self,length):
        return global_in.read(length,timeout=0).tobytes()
        
    def write_u32(self,x):
        try:
            global_out.write(struct.pack("<I", x))
        except:
            pass
        
    def write_u64(self,x):
        try:
            global_out.write(struct.pack("<Q", x))
        except:
            pass
        
    def write_string(self,x):
        try:
            self.write_u32(len(x))
            self.write(x.encode())
        except:
            pass
        
    def read_u32(self):
        return struct.unpack("<I", self.read(4))[0]
    
    def read_u64(self):
        return struct.unpack("<Q", self.read(8))[0]
    
    def read_string(self):
        return self.read(self.read_u32() + 1)[:-1].decode()
    
    def magic_ok(self):
        return self.GLUC == self.magic
        
    def is_id(self,a_cmd):
        return a_cmd == self.cmd_id
    
    def read_cmd(self):
        try:
            self.magic = self.read(4)
            self.cmd_id = self.read_u32()
        except:
            pass
        
    def write_cmd(self,a_cmd):
        try:
            self.write(self.magic)
            self.write_u32(a_cmd)
        except:
            pass

    def read_path(self):
        path = self.read_string()
        drive = path.split(":", 1)[0]
        try:
            path = path.replace(drive + ":", self.drives[drive])
        except KeyError:
            pass
        return path
    
    def process(self):
        while global_dev is not None and not task_canceled:
            self.read_cmd()
            if self.magic_ok():
                if self.is_id(GoldleafCommandId.ListSystemDrives):
                    drive_labels = {}
                    if "win" in sys.platform[:3].lower():
                        import string
                        import ctypes
                        kernel32 = ctypes.windll.kernel32
                        bitmask = kernel32.GetLogicalDrives()
                        for letter in string.ascii_uppercase:
                            if bitmask & 1:
                                self.drives[letter] = letter + ":/"
                                label_buf = ctypes.create_unicode_buffer(1024)
                                kernel32.GetVolumeInformationW(
                                    ctypes.c_wchar_p(letter + ":\\"),
                                    label_buf,
                                    ctypes.sizeof(label_buf),
                                    None,
                                    None,
                                    None,
                                    None,
                                    0
                                    )
                                if label_buf.value:
                                    drive_labels[letter] = label_buf.value
                            bitmask >>= 1
                    else:
                        self.drives["ROOT"] = "/"
                    self.write_u32(len(self.drives))
                    for d in self.drives:
                        try:
                            self.write_string(drive_labels[d])
                        except KeyError:
                            self.write_string(d)
                        self.write_string(d)
                elif self.is_id(GoldleafCommandId.GetEnvironmentPaths):
                    env_paths = {x:os.path.expanduser("~/"+x) for x in ["Desktop", "Documents"]}
                    for arg in sys.argv[1:]:
                        folder = os.path.abspath(arg)
                        if os.path.isfile(folder):
                            folder = os.path.dirname(folder)
                        env_paths[os.path.basename(folder)] = folder
                    env_paths = {x:env_paths[x] for x in env_paths if os.path.exists(env_paths[x])}
                    self.write_u32(len(env_paths))
                    for env in env_paths:
                        env_paths[env] = env_paths[env].replace("\\", "/")
                        self.write_string(env)
                        if env_paths[env][1:3] != ":/":
                            env_paths[env] = "ROOT:" + env_paths[env]
                        self.write_string(env_paths[env])
                elif self.is_id(GoldleafCommandId.GetPathType):
                    ptype = 0
                    path = self.read_path()
                    if os.path.isfile(path):
                        ptype = 1
                    elif os.path.isdir(path):
                        ptype = 2
                    self.write_u32(ptype)
                elif self.is_id(GoldleafCommandId.ListDirectories):
                    path = self.read_path()
                    ents = [x for x in os.listdir(path) if os.path.isdir(os.path.join(path, x))]
                    n_ents = []
                    for e in ents:
                        try:
                            test = os.listdir(os.path.join(path, e))
                            n_ents.append(e)
                        except:
                            pass
                    self.write_u32(len(n_ents))
                    for name in n_ents:
                        self.write_string(name)
                elif self.is_id(GoldleafCommandId.ListFiles):
                    self.fw_status = self.FW_NOSTATUS
                    if is_installing:
                        complete_goldleaf_transfer()
                    path = self.read_path()
                    ents = [x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x))]
                    if not allow_access_non_nsp:
                        len_nsps = 0
                        for f in ents:
                            if f.lower().endswith('.nsp'):
                                len_nsps = len_nsps+1
                        self.write_u32(len_nsps)
                        for name in ents:
                            if name.lower().endswith('.nsp'):
                                self.write_string(name)
                    else:
                        self.write_u32(len(ents))
                        for name in ents:
                            self.write_string(name)
                elif self.is_id(GoldleafCommandId.GetFileSize):
                    path = self.read_path()
                    self.write_u64(os.path.getsize(path))
                elif self.is_id(GoldleafCommandId.FileRead):
                    can_read = True
                    offset = self.read_u64()
                    size = self.read_u64()
                    path = self.read_path()
                    if not os.path.basename(path).lower().endswith('.nsp'):
                        if allow_access_non_nsp:
                            can_read = True
                        else:
                            can_read = False
                    if can_read:
                        with open(path, "rb") as f:
                            f.seek(offset)
                            data = f.read(size)
                        self.write_u64(len(data))
                        self.write(data)
                        try:
                            if self.fw_status != self.FW_DENIED:
                                complete_loading()
                                set_cur_nsp(str(os.path.basename(path)))
                                set_progress(int(offset), int(os.path.getsize(path)))
                                elapsed_time = time.time() - start_time
                                if elapsed_time >= 1:
                                    set_cur_transfer_rate(int(offset) - last_transfer_rate)
                                    set_last_transfer_rate(int(offset))
                                    set_start_time()
                            else:
                                complete_goldleaf_transfer()
                        except:
                            pass
                    else:
                        logging.debug("Error: Access denied. \nReason: Goldleaf tried to access a non .NSP file(to bypass this default restriction, change \'allow_access_non_nsp\' to 1 in fluffy.conf).")
                        print("Error: Access denied. \nReason: Goldleaf tried to access a non .NSP file(to bypass this default restriction, change \'allow_access_non_nsp\' to 1 in fluffy.conf).")
                        cancel_task()
                        sys.exit()
                elif self.is_id(GoldleafCommandId.FileWrite):
                    offset = self.read_u64()
                    size = self.read_u64()
                    path = self.read_path()
                    data = self.read(size)
                    can_write = False
                    if self.fw_status == self.FW_NOSTATUS:
                        get_response_qmessage(1)
                        while not haveresponse and global_dev is not None:                    
                            time.sleep(1)
                        if qresponse:
                            self.fw_status = self.FW_ACCEPTED
                            can_write = True
                        else:
                            self.fw_status = self.FW_DENIED
                    elif self.fw_status == self.FW_ACCEPTED:
                        can_write = True
                    if can_write:
                        cont = bytearray()
                        try:
                            with open(path, "rb") as f:
                                cont=bytearray(f.read())
                        except FileNotFoundError:
                            pass
                        cont[offset:offset + size] = data
                        with open(path, "wb") as f:
                            f.write(cont)
                    reset_response()
                elif self.is_id(GoldleafCommandId.CreateFile):
                    path = self.read_path()
                    get_response_qmessage(2)
                    while not haveresponse and global_dev is not None:                    
                        time.sleep(1)
                    if qresponse:
                        open(path, "a").close()
                    reset_response()
                elif self.is_id(GoldleafCommandId.CreateDirectory):
                    path = self.read_path()
                    get_response_qmessage(3)
                    while not haveresponse and global_dev is not None:                    
                        time.sleep(1)
                    if qresponse:
                        try:
                            os.mkdir(path)
                        except os.FileExistsError:
                            pass
                    reset_response()
                elif self.is_id(GoldleafCommandId.DeleteFile):
                    path = self.read_path()
                    get_response_qmessage(4)
                    while not haveresponse and global_dev is not None:                    
                        time.sleep(1)
                    if qresponse:
                        os.remove(path)
                    reset_response()
                elif self.is_id(GoldleafCommandId.DeleteDirectory):
                    path = self.read_path()
                    get_response_qmessage(5)
                    while not haveresponse and global_dev is not None:                    
                        time.sleep(1)
                    if qresponse:
                        shutil.rmtree(path)
                    reset_response()
                elif self.is_id(GoldleafCommandId.RenameFile):
                    path = self.read_path()
                    new_name = self.read_string()
                    get_response_qmessage(6)
                    while not haveresponse and global_dev is not None:                    
                        time.sleep(1)
                    if qresponse:
                        os.rename(path, new_name)
                    reset_response()
                elif self.is_id(GoldleafCommandId.RenameDirectory):
                    path = self.read_path()
                    new_name = self.read_path()
                    get_response_qmessage(6)
                    while not haveresponse and global_dev is not None:                    
                        time.sleep(1)
                    if qresponse:
                        os.rename(path, new_name)
                    reset_response()
                elif self.is_id(GoldleafCommandId.GetDriveTotalSpace):
                    path = self.read_path()
                    disk = os.statvfs(path)
                    totalBytes = float(disk.f_bsize*disk.f_blocks)
                    self.write_u64(int(totalspace))
                elif self.is_id(GoldleafCommandId.GetDriveFreeSpace):
                    path = self.read_path()
                    disk = os.statvfs(path)
                    totalFreeSpace = float(disk.f_bsize*disk.f_bfree)
                    self.write_u64(int(totalFreeSpace))
        sys.exit()