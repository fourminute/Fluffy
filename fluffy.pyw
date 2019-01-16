"""""
MIT License

Copyright (c) 2019 fourminute

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""""

import os
import sys
import threading
import struct
from binascii import hexlify as hx, unhexlify as uhx
from pathlib import Path
from tkinter import messagebox
import tkinter as tk
from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import Progressbar
from tkinter import filedialog
import logging
LOG_FILENAME = 'fluffy.log'
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)
root = tk.Tk()
root.withdraw()
try:
    import usb.core
    import usb.util
except ImportError:
    messagebox.showinfo("Error","PyUSB not found. Please install with 'pip3 install pyusb'\nIf you are on MacOS, also install LibUSB with 'brew install libusb'. For more info on brew, head to https://brew.sh/.\n\nAlso ensure you have ONLY the latest Python 3 installed on your machine. Having previous versions of Python 3 installed can cause this error to occur.")
    exit()

installing = False
is_done = False
is_loading = True
selected_dir = None
selected_files = None
exit_status = False
last_name_len = 0
last_data_size = 0
cur = 0
end = 0
count = 1
total_nsp = 0

def set_dir(d):
    global selected_dir
    selected_dir = d
    
def set_selected(f):
    global selected_files
    selected_files = f

def give_up_usb():
    global installing
    installing = True
    
def set_progress(c, e):
    global cur
    global end
    end = e
    cur = c
    
def get_count():
    global count
    return count

    
def get_cur():
    global cur
    return cur

def get_end():
    global end
    return end

def set_count(n, d):
    global last_name_len
    global last_data_size
    global count
    if last_name_len != n:
        if last_data_size != d:
            if not last_data_size == 0:
                count += 1
                last_data_size = d
                last_name_len = n
            else:
                last_data_size = d
                last_name_len = n

def set_total_nsp(n):
    global total_nsp
    total_nsp = n
    
def get_total_nsp():
    global total_nsp
    return total_nsp

def complete_install():
    global is_done
    is_done = True
    
def complete_loading():
    global is_loading
    is_loading = False

CMD_ID_EXIT = 0
CMD_ID_FILE_RANGE = 1
CMD_TYPE_RESPONSE = 1

def send_response_header(out_ep, cmd_id, data_size):
    out_ep.write(b'TUC0') # Tinfoil USB Command 0
    out_ep.write(struct.pack('<B', CMD_TYPE_RESPONSE))
    out_ep.write(b'\x00' * 3)
    out_ep.write(struct.pack('<I', cmd_id))
    out_ep.write(struct.pack('<Q', data_size))
    out_ep.write(b'\x00' * 0xC)

def file_range_cmd(nsp_dir, in_ep, out_ep, data_size):
    file_range_header = in_ep.read(0x20)
    range_size = struct.unpack('<Q', file_range_header[:8])[0]
    range_offset = struct.unpack('<Q', file_range_header[8:16])[0]
    nsp_name_len = struct.unpack('<Q', file_range_header[16:24])[0]
    set_count(int(nsp_name_len), int(data_size))
    nsp_name = bytes(in_ep.read(nsp_name_len)).decode('utf-8')
    print('Range Size: {}, Range Offset: {}, Name len: {}, Name: {}'.format(range_size, range_offset, nsp_name_len, nsp_name))
    send_response_header(out_ep, CMD_ID_FILE_RANGE, range_size)

    with open(nsp_name, 'rb') as f:
        f.seek(range_offset)
        curr_off = 0x0
        end_off = range_size
        read_size = 0x100000
        while curr_off < end_off:
            if exit_status:
                break
            if curr_off + read_size >= end_off:
                read_size = end_off - curr_off
                try:
                    set_progress(int(end_off), int(end_off))
                except:
                    pass
            buf = f.read(read_size)
            out_ep.write(data=buf, timeout=0)
            curr_off += read_size
            try:
                set_progress(int(curr_off), int(end_off))
            except:
                pass

def poll_commands(nsp_dir, in_ep, out_ep):
    while True:
        if exit_status:
            break
        cmd_header = bytes(in_ep.read(0x20, timeout=0))
        magic = cmd_header[:4]
        #print('Magic: {}'.format(magic), flush=True)
        if magic != b'TUC0': # Tinfoil USB Command 0
            continue
        cmd_type = struct.unpack('<B', cmd_header[4:5])[0]
        cmd_id = struct.unpack('<I', cmd_header[8:12])[0]
        data_size = struct.unpack('<Q', cmd_header[12:20])[0]
        #print('Cmd Type: {}, Command id: {}, Data size: {}'.format(cmd_type, cmd_id, data_size), flush=True)
        if cmd_id == CMD_ID_EXIT:
            #print('Exiting...')
            complete_install()
            break
        elif cmd_id == CMD_ID_FILE_RANGE:
            file_range_cmd(nsp_dir, in_ep, out_ep, data_size)

def send_nsp_list(s_f, nsp_dir, out_ep):
    nsp_path_list = list()
    nsp_path_list_len = 0
    for nsp_path in [f for f in nsp_dir.iterdir() if f.is_file() and f.suffix == '.nsp']:
        for y in s_f:
            if str(nsp_path).find(os.path.basename(y)) != -1:
                nsp_path_list.append(nsp_path.__str__() + '\n')
                nsp_path_list_len += len(nsp_path.__str__()) + 1
    print('Sending header...')
    out_ep.write(b'TUL0') # Tinfoil USB List 0
    out_ep.write(struct.pack('<I', nsp_path_list_len))
    out_ep.write(b'\x00' * 0x8) # Padding
    print('Sending NSP list: {}'.format(nsp_path_list))
    complete_loading()
    for nsp_path in nsp_path_list:
        out_ep.write(nsp_path)
        
def init_usb_install(args, s_f):
    nsp_dir = Path(args)
    if not nsp_dir.is_dir():
        raise ValueError('1st argument must be a directory')
    dev = usb.core.find(idVendor=0x057E, idProduct=0x3000)
    if dev is None:
        raise ValueError('Switch is not found!')
    dev.reset()
    dev.set_configuration()
    cfg = dev.get_active_configuration()
    is_out_ep = lambda ep: usb.util.endpoint_direction(ep.bEndpointAddress) == usb.util.ENDPOINT_OUT
    is_in_ep = lambda ep: usb.util.endpoint_direction(ep.bEndpointAddress) == usb.util.ENDPOINT_IN
    out_ep = usb.util.find_descriptor(cfg[(0,0)], custom_match=is_out_ep)
    in_ep = usb.util.find_descriptor(cfg[(0,0)], custom_match=is_in_ep)
    assert out_ep is not None
    assert in_ep is not None
    send_nsp_list(s_f, nsp_dir, out_ep)
    poll_commands(nsp_dir, in_ep, out_ep)


def switch_connected():
    while True:
        if exit_status:
            break
        if installing == False:
            dev = usb.core.find(idVendor=0x057E, idProduct=0x3000)
            if dev is None:
                lbl_switch.config(text="Switch Not Detected!",fg="dark red", font='Helvetica 9 bold')
            else:
                lbl_switch.config(text="Switch Detected!",fg="dark green", font='Helvetica 9 bold')
        else:
            break

def update_progress():
    while True:
        if exit_status:
            break
        last_c = 1
        try:
            if is_loading == False:
                c = get_cur()
                e = get_end()
                v = (int(c) / int(e)) * 100
                bar['value'] = v
                cur_c = get_count()
                if is_done:
                    lbl_status.config(text="Successfully Installed " + str(get_total_nsp()) + " NSPs!", fg="dark blue", font='Helvetica 9 bold')
                    window.update_idletasks()
                    window.update()
                    break
                else:
                    lbl_switch.config(text="Progress: " + str(round(v, 2)) + "%",fg="dark green", font='Helvetica 9 bold')
                lbl_status.config(text="Installing " + str(cur_c) + " of " + str(get_total_nsp()) + " NSPs.")
                window.update_idletasks()
                window.update()
            else:
                lbl_status.config(text="Loading " + str(get_total_nsp()) + " NSPs. Please Wait.")
        except:
            pass

def usb_thread():
    try:
        give_up_usb()
        init_usb_install(selected_dir, selected_files)
    except Exception as e:
        logging.error(e, exc_info=True)
        exit()


    
def send():
    try:
        btn.config(state="disabled")
        btn2.config(state="disabled")
        threading.Thread(target = usb_thread).start()
        threading.Thread(target = update_progress).start()
    except Exception as e:
        logging.error(e, exc_info=True)
        exit()


# UI
try:
    window = Tk()
    window.resizable(0,0)
    window.title("Fluffy")
    window.iconbitmap(r'icon.ico')
    window.geometry('237x235')
    lbl_status = tk.Label(window)
    lbl_switch = tk.Label(window)
    lbl_status.config(text="Select a folder.", font='Helvetica 9 bold')
    lbl_switch.config(text="Switch Not Detected!",fg="dark red", font='Helvetica 9 bold')
    def get_folder():
        d = filedialog.askopenfilenames(parent=window,title='Select NSPs',filetypes=[("NSP files", "*.nsp")])
        set_dir(os.path.dirname(d[0]))
        file_list = list(d)
        tmp = list()
        listbox.delete(0, tk.END)
        i = 0
        for f in file_list:
            if f.endswith(".nsp"):
                i += 1
                listbox.insert(END,str(os.path.basename(f)))
                tmp.append(f)
        if i > 0:
            btn2.config(state="normal")
            set_total_nsp(i)
            set_selected(tmp)
            lbl_status.config(text=str(get_total_nsp()) + " NSPs Selected.")
        else:
            btn2.config(state="disabled")
            lbl_status.config(text="Select a folder.", font='Helvetica 9 bold')
    listbox = Listbox(window)

    btn = Button(window, text="Select NSPs", command=get_folder)
    btn2 = Button(window, text="Send Header", command=send)
    btn2.config(state="disabled")
    bar = Progressbar(window)
    bar['value'] = 0
    btn.pack(side=TOP,padx=3,pady=(3,0),fill=X)
    btn2.pack(side=TOP,padx=3,pady=(3,0),fill=X)
    lbl_status.pack(side=TOP,padx=3,pady=(3,0),fill=X)
    lbl_switch.pack(side=TOP,padx=3,pady=(3,0),fill=X)
    bar.pack(side=TOP,padx=3,pady=(3,0),fill=X)
    listbox.pack(side=TOP,padx=3,pady=(3,5),fill=X)
    listbox.config(height=7)
    def close_program():
        global exit_status
        if installing:
            if is_done == False:
                if messagebox.askokcancel("Quit", "Quitting during installation can cause corruption.\nCancel current installation and quit?"):
                    exit_status = True
                    exit()
            else:
                exit_status = True
                exit()
        else:
            exit()
    window.protocol("WM_DELETE_WINDOW", close_program)
    threading.Thread(target = switch_connected).start()
    window.mainloop()
except Exception as e:
    logging.error(e, exc_info=True)
    exit()
