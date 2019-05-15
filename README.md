# Fluffy
![intro](https://github.com/fourminute/Fluffy/blob/master/misc/fluffy-intro.png?raw=true)
 <b><a href="https://github.com/fourminute/Fluffy/blob/master/README_CH.md">查看中文使用说明，请点击这里！</a></b>
 
#### All donations are appreciated! Thank you if you decide to donate!
* <b>Monero</b>:  4APPsi7nnAs4ZjGC58V5CjVnceEvnZbY1WCBSjmcQsKhGPWLL2EaoUDU2RVFnuLEnASRA2ECXD4YvQ8hyVyZg1raJ482yei

### <b><a href="https://github.com/fourminute/Fluffy/releases/latest">Latest Release v2.7.1</a></b>
### <b><a href="https://github.com/fourminute/Fluffy/blob/master/Tinfoil.nro">Download Recommended TinFoil.nro</a></b>

## Features
* Support for <b>XorTroll/Goldleaf</b> and <b>Adubbz/Tinfoil</b>
* Support for languages: <b>English, Chinese, Vietnamese, Spanish, French, Brazilian Portuguese, Turkish, Italian, German and Bahasa Indonesia</b>!
* Ability to abort an installation in queue.
* USB and Network Install, display transfer rate in MB/s and progress percentage.
* USB and Network Install, display current NSP being installed.
* Goldleaf: Display current NCA being installed.
* Goldleaf: Display current NCA queue. 
* Transfer modes between "Normal" and "Safe".
* Smart User-Interface, switches between Tkinter and PyQt depending on modules installed. (<b>v1.4.1 and below only</b>)
* Support for UI scaling on 4K, 1080P, and 720P displays.
* Show current NSP being installed.
* Individual NSP selection (suggest by: <b>Shadowhand</b>, thanks!).
* Tasty donut.
* Switch connected indicator.
* 5.x USB Fix (Thanks to <a href="https://github.com/satelliteseeker">satelliteseeker</a>)

# Screenshot
![screenshot](https://github.com/fourminute/Fluffy/blob/master/misc/screenshotv250b.png?raw=true)


# Instructions For Use

## Install TinFoil on your Switch
* <b>These steps apply for all custom firmware. This includes but not limited to: Kosmos, ReINX, SXOS, etc.</b>
* Download <a href="https://github.com/fourminute/Fluffy/blob/master/Tinfoil.nro">Recommended TinFoil</a>
* Copy and paste "<b>TinFoil.nro</b>" to a folder named "Switch"(create it if necessary) on the root of your SD card.

## Windows instructions

### 1/3) Install and Setup Zadig Driver
* Download Zadig: https://zadig.akeo.ie or [github mirror](https://github.com/fourminute/Fluffy/blob/master/windows/zadig-2.4.exe) in case the website goes down.
* With your Switch plugged in to your PC using a USB-C cable, open TinFoil(on your Switch). This will ensure your Switch is visible.
* Open Zadig > Options > List All Devices.
* In the scroll box above the button "Install Driver", tap the arrow until arriving at "libusbK".
* Click "Install Driver"
* Done!

### 2/3) Install Python
* Download and Install Python 3 from [Python Website](https://www.python.org/downloads/). Select the "PATH" option during install. <b>Ensure no previous version of Python is installed and do not use the 64-bit version of Python 3. This may cause an error "PyUSB not found".</b> Also be sure to include Tkinter with your installation(it should be a default option).

### 3/3) Install PyUSB, LibUSB, PyQt5, QDarkStyle
* Open Command-line/CMD (Start, search "CMD") and run the following:
```
pip3 install pyusb pyqt5 libusb libusb1 qdarkstyle configparser
```

### Additional Windows Instructions
Some users may receive the error "USB.Core No Backend Available". If you do, download this .DLL file [libusb.dll](https://github.com/fourminute/Fluffy/blob/master/windows/libusb-1.0.dll) and place it in the same directory as Fluffy.pyw.

If you still receive this error, you can try installing LibUSB: [libusb installer](https://github.com/fourminute/Fluffy/blob/master/windows/libusb-win32-devel-filter-1.2.6.0.exe).

## Linux instructions

### Ubuntu/Debian based distributions

#### 1/2) Install Python and Dependencies
* Required: ```python3 python3-pyusb python3-pyqt5 python3-tk python3.6-tk libusb libusb1 qdarkstyle```.
* Install Python3:
* ```sudo apt install python3 python3-pip python3-tk```.
* Then open Terminal and run this command:
* ```pip3 install pyusb pyqt5 libusb libusb1 qdarkstyle configparser```.

#### 2/2) Download Fluffy and Switch Rule
Download the latest <a href="https://github.com/fourminute/Fluffy/releases/latest">Fluffy.pyw</a> and <a href="https://github.com/fourminute/Fluffy/blob/master/linux/80-fluffy-switch.rules">80-fluffy-switch.rules</a>.

Open Terminal and change into the directory where these files are located using the cd command:
 ```
 cd /path/to/fluffy/
 ```
 
Copy the file <b>80-fluffy-switch.rules</b> to <b>/etc/udev/rules.d/</b> using this command:
```
sudo cp 80-fluffy-switch.rules /etc/udev/rules.d/
```
Then give both the proper permissions:
```
sudo chmod 644 /etc/udev/rules.d/80-fluffy-switch.rules
sudo chmod 755 fluffy.pyw
```

### Arch/Manjaro/Antergos
Install the AUR package <a href="https://aur.archlinux.org/packages/fluffy-switch/">fluffy-switch</a> maintained by <a href="https://github.com/YoyPa">YoyPa</a>.


### Installation and Application Launcher (Optional)
You may wish to Install Fluffy. Download the latest <a href="https://github.com/fourminute/Fluffy/releases/latest">Fluffy.pyw</a> and 'icon.ico' and 'install.sh' from <a href="https://github.com/fourminute/Fluffy/tree/master/linux">here</a>. Extract and move each file into a single folder.

Installation is then as simple as:
```
cd /path/to/files/
sudo ./install.sh
```
## MacOS instructions
```
 brew install libusb 
 brew reinstall python --with-tcl-tk
 pip3 install configparser
```
<i>For more info on brew, head to https://brew.sh/</i>

## How-To-Use
Complete beginner? No problem. 
* <b>First follow the installation steps above. Done? Let's continue!</b>
* On your Switch running Custom Firmware open TinFoil > Title Management > USB Install NSP.
* Double-click on Fluffy.pyw to start it (Linux users: type ```fluffy``` in your start menu or terminal).
* Click "Select NSPs" and select as many NSPs as you want to install.
* If "Switch Detected!" is visible. Click "Begin Transfer".
* On your Switch, select and install the NSPs.

## Troubleshooting Tips
<b>Why do I keep getting the error: "USBCore No Backend Available"?</b>

Answer: This can be caused by 1-2 things.

1) Not all USB type C cables will work with the Switch. If your Switch connects then frequently disconnects, then reconnects again, etc. Or if you receive this error, it's highly likely you will need a newer USB type C cable. Yes, there are differences despite being visually similar.

2) LibUSB wasn't found. Install it with "pip3 install libusb" and "pip3 install libusb1". Also follow the above steps labeled "Additional Windows Instructions".

<b>Why do I keep getting the error: "No module named 'PyQt5'"?</b>

Python by default *wants* to run in 64-bit mode, however, when this happens Fluffy won't work. As you may already know, Fluffy does not, will not, and cannot run in 64-bit Python. To bypass this behavior you can alternative open Fluffy.pyw in IDLE(32-bit mode) and click Run > Run Module.


<b>Why does network install fail?</b>

Answer: Network install is a hit or miss depending on your setup. Try forwarding port 2000 in your router and disabling your firewall. Ensure your Switch and PC are on the same network.

<b>PyUSB Not Found and I've followed all the steps!</b>

Answer: **Fluffy only works with Python 3 32-bit version.** Also be ensure no previous versions of Python are installed. If necessary, uninstall them. For example, if you have Python 3.6.6 and Python 3.7.2 installed at the same time Fluffy may throw this error.

<b>What kind of cable does the Switch use?</b>

Answer: USB type C cable. Though, not all USB type C cables are the same. Some will not be compatible with the Switch.

<b>Does Fluffy work on MacOS and Linux?</b>

Answer: Absolutely! Python is cross-platform and so Fluffy should work on both operating systems.

<b>Which Custom Firmware works best with Fluffy and TinFoil?</b>

Answer: All of them will work the same. That is up to you.

<b>Why does my install keeps hanging and/or crashing?</b>

Answer: Switch Transfer Mode to "Safe".

<b>Why do I have unsufficient permission error (usb)(linux)? (credit: YoyPa)</b>

Answer: You need to make a <a href=https://github.com/fourminute/Fluffy/blob/master/linux/80-fluffy-switch.rules>udev rule</a> to modify the switch usb device permission in /etc/udev/rules.d/

<b>Still having problems? Consider making a bug report on this GitHub page to request assistance.</b>

<i>Disclaimer: The "Pink Donut" design was designed by fourminute exclusively for Fluffy and infringes on no copyright. The font used in "intro.png" is also 100% royalty free.</i>
