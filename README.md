# Fluffy
![intro](https://github.com/fourminute/Fluffy/blob/master/misc/may_intro_v4.png?raw=true)
 <b><a href="https://github.com/fourminute/Fluffy/blob/master/README_CH.md">查看中文使用说明，请点击这里！</a></b>
 
 <b><a href="https://github.com/fourminute/Fluffy/blob/master/README_KR.md">한국어를 할 줄 알아요?</a></b>

![License](https://img.shields.io/badge/License-GPLv3-blue.svg) [![Releases](https://img.shields.io/github/downloads/fourminute/fluffy/total.svg)]() [![LatestVer](https://img.shields.io/github/release-pre/fourminute/fluffy.svg)]()

### <b><a href="https://github.com/fourminute/Fluffy/releases/latest">Latest Release v2.9.2</a></b>
### <b><a href="https://github.com/fourminute/Fluffy/raw/master/Tinfoil.nro">Download Recommended TinFoil.nro</a></b>
### <b><a href="https://github.com/fourminute/Fluffy/raw/master/Goldleaf.nro">Download Recommended Goldleaf.nro</a></b>


## Features
* Support for <b>XorTroll/Goldleaf</b> and <b>Adubbz/Tinfoil</b>
* Support for languages: <b>English, Chinese, Vietnamese, Spanish, French, Brazilian Portuguese, Turkish, Italian, German, and Bahasa Indonesia</b>!
* Cross platform: Fluffy works natively on <b>Windows</b>, <b>Linux</b>, and <b>MacOS</b>!
* USB and Network: Display live transfer rate in MB/s with progress percentage.
* USB and Network: Display current NSP being installed and numbered queue.
* USB and Network: Batch NSP install support with individual selection.
* USB and Network: Consecutive installs without restart. 
* USB and Network: Exception/Error handling, no restart required when an installation fails.
* USB and Network: Ability to abort an installation in queue.
* Tinfoil Network: Spoof file URL's to fix lengthy file name bug in Tinfoil's code.
* Tinfoil Network: Randomized port selection.
* Tinfoil Network: By default fall-back to Network Mode in the event USB mode can't be used(e.g. missing libraries).
* Goldleaf: Display current file being accessed.
* Goldleaf: Goldleaf v0.6 compatible with all of the file handling features.
* Goldleaf: Default protections are in place to safe-guard users from a potentially compromised Goldleaf file.
	* Default: File operations such as file creation, deletion, renaming will result in a user-prompt(yes or no).
	* Default: Read-only access for all files.
	* Default: Read/write to non-NSP files are restricted.
	* All of these security restrictions are changeable in fluffy.conf.
* Tinfoil USB: Selectable transfer rates between "Normal Mode" and "Safe Mode" for those with aging hardware(e.g. out of spec USB ports).
* USB: Switch connected indicator.
* User-Interface: Light Mode and Dark Mode.
* General: Auto saves to config Switch IP Address, Light/Dark Mode Settings, and Language Selection.
* General Support for UI scaling up to 4K resolution.
* Tinfoil USB: Switch Firmware 5.x USB Fix (Thanks to <a href="https://github.com/satelliteseeker">satelliteseeker</a> for finding this fix, choose 'Safe Mode')
* Cute fluffy penguin.

# Screenshot

<img src="https://github.com/fourminute/Fluffy/blob/master/misc/uifluffy-sq3.png?raw=true" width="800"/>

# [Windows] Instructions For Use (Fluffy.exe)

## 1/3) Install TinFoil or Goldleaf on your Switch
* <b>These steps apply for all custom firmware. This includes but not limited to: Kosmos, ReINX, SXOS, etc.</b>
* Download <a href="https://github.com/fourminute/Fluffy/blob/master/Tinfoil.nro">Recommended TinFoil</a>
* Copy and paste "<b>TinFoil.nro</b>" to a folder named "Switch"(create it if necessary) on the root of your SD card.
* <i>or</i>  Download <a href="https://github.com/XorTroll/Goldleaf/releases">Goldleaf</a> by XorTroll.

### 2/3) Install and Setup Zadig Driver
* Download Zadig: https://zadig.akeo.ie or [github mirror](https://github.com/fourminute/Fluffy/blob/master/windows/zadig-2.4.exe) in case the website goes down.
* With your Switch plugged in to your PC using a USB-C cable, open TinFoil(on your Switch). This will ensure your Switch is visible.
* Open Zadig > Options > List All Devices.
* In the scroll box above the button "Install Driver", tap the arrow until arriving at "libusbK".
* Click "Install Driver"
* Done!

### 3/3) Run Fluffy and Install NSP(s)! (Tinfoil)
* Connect your Switch and your PC with a USB Type-C cable.
* Run Fluffy.exe.
* On your Switch open Tinfoil > Title Management > USB Install NSP
* On Fluffy click "NSP Selection" > Select your NSP(s)
* On Fluffy's Tinfoil USB screen click "Begin Transfer".

### 3/3) Run Fluffy and Install NSP(s)! (Goldleaf)
* Run Fluffy.exe.
* On your Switch open Goldleaf > Explore Content
* On Fluffy's Goldleaf screen click "Begin Transfer".
* On your Switch select "PC Drive (via USB)"
* Navigate to and install your NSP(s).

# [Windows] Instructions For Use (Fluffy.pyw)

## 1/5) Install TinFoil or Goldleaf on your Switch
* <b>These steps apply for all custom firmware. This includes but not limited to: Kosmos, ReINX, SXOS, etc.</b>
* Download <a href="https://github.com/fourminute/Fluffy/blob/master/Tinfoil.nro">Recommended TinFoil</a>
* Copy and paste "<b>TinFoil.nro</b>" to a folder named "Switch"(create it if necessary) on the root of your SD card.
* <i>or</i>  Download <a href="https://github.com/XorTroll/Goldleaf/releases">Goldleaf</a> by XorTroll.

### 2/5) Install and Setup Zadig Driver
* Download Zadig: https://zadig.akeo.ie or [github mirror](https://github.com/fourminute/Fluffy/blob/master/windows/zadig-2.4.exe) in case the website goes down.
* With your Switch plugged in to your PC using a USB-C cable, open TinFoil(on your Switch). This will ensure your Switch is visible.
* Open Zadig > Options > List All Devices.
* In the scroll box above the button "Install Driver", tap the arrow until arriving at "libusbK".
* Click "Install Driver"
* Done!

### 3/5) Install Python
* Download and Install Python 3 from [Python Website](https://www.python.org/downloads/). Select the "PATH" option during install. <b>Ensure no previous version of Python is installed and do not use the 64-bit version of Python 3. This may cause an error "PyUSB not found".</b> Also be sure to include Tkinter with your installation(it should be a default option).

### 4/5) Install Python Dependencies
* Open Command-line/CMD (Start, search "CMD") and run the following:
```
pip3 install pyusb pyqt5 libusb libusb1 qdarkstyle configparser
```

### 5/5) Run Fluffy and Install NSP(s)! (Tinfoil)
* Connect your Switch and PC with a USB Type-C cable
* Run Fluffy.pyw
* On your Switch open Tinfoil > Title Management > USB Install NSP
* On Fluffy click "NSP Selection" > Select your NSP(s)
* On Fluffy's Tinfoil USB screen click "Begin Transfer"

### 5/5) Run Fluffy and Install NSP(s)! (Goldleaf)
* Connect your Switch and PC with a USB Type-C cable
* Run Fluffy.pyw
* On your Switch open Goldleaf > Explore Content
* On Fluffy's Goldleaf screen click "Begin Transfer"
* On your Switch select "PC Drive (via USB)"
* Navigate to and install your NSP(s)

## Linux instructions

### Ubuntu/Debian based distributions

#### 1/3) Install Python and Dependencies
* Required: ```python3 python3-pyusb python3-pyqt5 python3-tk python3.6-tk libusb libusb1 qdarkstyle```.
* Install Python3:
* ```sudo apt install python3 python3-pip python3-tk```.
* Then open Terminal and run this command:
* ```pip3 install pyusb pyqt5 libusb libusb1 qdarkstyle configparser```.
* If that doesn't work try
* ```pip install pyusb pyqt5 libusb libusb1 qdarkstyle configparser```.

#### 2/3) Download Fluffy and Switch Rule
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
#### 3/3) Starting Fluffy
To start Fluffy.pyw you should be able to double-click to open. But if that doesn't work, you may need to run Fluffy.pyw using Terminal.

Open Terminal and Enter:
```
python3 /path/to/fluffy.pyw
```
<i>Alternatively</i>, you can install IDLE(A Python interface).
```
sudo apt-get install idle3
```
Open IDLE > Open Fluffy.pyw then select Run > Run Module.

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
brew install tcl-tk
brew reinstall python3
pip3 install pyusb pyqt5 libusb libusb1 qdarkstyle configparser
python3 ./fluffy.pyw
```
<sub>Special thanks to <a href="https://github.com/GuillaumeJulien">GuillaumeJulien</a> for these instructions.</sup>

<sub><i>For more info on brew, head to https://brew.sh/</i></sup>


## Troubleshooting Tips
<b>(Linux)Fluffy.pyw still shows up as an unknown file?</b>

Answer: Run it using Terminal
```
python3 fluffy.pyw
```

<b>Why do I keep getting the error: "USBCore No Backend Available"?</b>

Answer: This can be caused by 1-2 things.

1) Download <a href="https://github.com/fourminute/Fluffy/raw/master/windows/libusb-1.0.dll">libusb-1.0.dll</a> and place it in the same folder as Fluffy. If that doesn't work, install LibUSB using Zadig or <a href="https://github.com/fourminute/Fluffy/raw/master/windows/libusb-win32-devel-filter-1.2.6.0.exe">libusb-win32-devel-filter Installer</a>.

2) Not all USB Type-C cables will work with the Switch. If your Switch connects then frequently disconnects, then reconnects again, etc. Or if you receive this error, it's highly likely you will need a newer USB Type-C cable. Yes, there are differences despite being visually similar.

<b>Why do I keep getting the error: "No module named 'PyQt5'"?</b>

Ensure "PATH" is selected when installing Python. If that still doesn't solve it, try running Fluffy using IDLE(32-bit mode).

<b>Why does network install hang/freeze?</b>

Answer: This is normal. Network install can sometimes hang and take a long time to work depending on your nework, how many devices are using your WiFi, your WiFi speed, etc. Give it some time and it will initiate the transfer. It may take several minutes. Fluffy may seem frozen, but in most instances a little patience is advisable.

<b>What kind of cable does the Switch use?</b>

Answer: USB Type-C cable. Though, not all USB Type-C cables are the same. Some will not be compatible with the Switch. 

<b>Does Fluffy work on MacOS and Linux?</b>

Answer: Absolutely! Python is cross-platform and so Fluffy should work on both operating systems.

<b>Which Custom Firmware works best with Fluffy and TinFoil?</b>

Answer: All of them will work the same. That is up to you.

<b>Why does my install keep hanging and/or crashing?</b>

Answer: Switch Transfer Mode to "Safe Mode". If you're installing via Tinfoil Network, it is normal for the install to sometimes hang.

<b>Why do I have unsufficient permission error (usb)(linux)? (credit: YoyPa)</b>

Answer: You need to make a <a href=https://github.com/fourminute/Fluffy/blob/master/linux/80-fluffy-switch.rules>udev rule</a> to modify the switch usb device permission in /etc/udev/rules.d/

<b>Still having problems? Consider making a bug report on this GitHub page to request assistance.</b>


## Credits

Fluffy was developed from the ground-up by Fourminute, including almost all of the features and bug fixes throughout. But there have been several people that have devoted their time and effort into improving Fluffy.

I would like to extend my thanks to the people below for helping make Fluffy what it is today.

* <a href="https://github.com/wendyliga">wendyliga</a> for their Bahasa Indonesia translation.
* <a href="https://github.com/TheLastZombie">TheLastZombie</a> for their German translation.
* <a href="https://github.com/YoyPa">YoyPa</a> for their many and various code contributions, creating and maintaining the <a href="https://aur.archlinux.org/packages/fluffy-switch/">fluffy-switch</a> AUR package, as well as their Spanish and French translations.
* LoOkYe for testing and debugging Fluffy in its various stages of development on MacOS.
* <a href="https://github.com/friedkeenan">friedkeenan</a> for their tremendous help on Goldleaf v0.6 compatibility.
* <a href="https://github.com/TorpedoXL">TorpedoXL</a> for their Turkish translation.
* <a href="https://github.com/DavidOliM">DavidOliM</a> for their Brazilian Portuguese translation.
* <a href="https://github.com/danypava">danypava</a> for their Italian translation.
* <a href="https://github.com/Sev73n">Sev73n</a> for their Chinese(Mandarin) translation as well as translating the entire README.

To anyone else that I missed, thank you.

<i>"Cute Penguin" was designed by fourminute. The font
used in the "Fluffy" logo is 100% royalty free.

Fluffy(this program) and the "Cute Penguin"
design is Copyright (c) 2019 fourminute
(https://github.com/fourminute)</i>
