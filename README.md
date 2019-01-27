# Fluffy
![intro](https://github.com/fourminute/Fluffy/blob/master/misc/fluffy-intro.png?raw=true)

### <b><a href="https://github.com/fourminute/Fluffy/releases/tag/v2.4">Latest Release v2.4.0</a></b>
### <b><a href="https://github.com/fourminute/Fluffy/blob/master/Tinfoil.nro">Download Recommended TinFoil.nro</a></b>

## Features
* Support for <b>XorTroll/Goldleaf</b> and <b>Adubbz/Tinfoil</b>
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
![screenshot](https://github.com/fourminute/Fluffy/blob/master/misc/screenshot-fluffy-v240c.png?raw=true)


# Instructions For Use
## Install and Setup Zadig Driver (Windows 10)
* Download Zadig: https://zadig.akeo.ie or [github mirror](https://github.com/fourminute/Fluffy/blob/master/windows/zadig-2.4.exe) in case the website goes down.
* With your Switch plugged in to your PC using a USB-C cable, open TinFoil(on your Switch). This will ensure your Switch is visible.
* Open Zadig > Options > List All Devices.
* In the scroll box above the button "Install Driver", tap the arrow until arriving at "libusbK".
* Click "Install Driver"
* Done!

## Install Python
* Download and Install Python 3 from [Python Website](https://www.python.org/downloads/). Select the "PATH" option during install. <b>Ensure no previous version of Python is installed and do not use the 64-bit version of Python 3. This may cause an error "PyUSB not found".</b>

## Install PyUSB, LibUSB, PyQt5, QDarkStyle
* Open Terminal/Command-line/CMD and run the following:
* pip3 install pyqt5 pyusb libusb libusb1 qdarkstyle

## Additional Windows Instructions
Some users may receive the error "USB.Core No Backend Available". If you do, download this .DLL file [libusb.dll](https://github.com/fourminute/Fluffy/blob/master/windows/libusb-1.0.dll) and place it in the same directory as Fluffy.pyw.

If you still receive this error, you can try installing LibUSB: [libusb installer](https://github.com/fourminute/Fluffy/blob/master/windows/libusb-win32-devel-filter-1.2.6.0.exe).

## Additional Linux instructions
### Switch Rules.d Config
By default, Linux imposes restrictions on USB devices. Without setting a <b>rule</b> for the Switch, Fluffy won't be able to communicate.
* Right-click this link and click "Save link as..." [80-fluffy-switch.rules](https://raw.githubusercontent.com/fourminute/Fluffy/master/linux/80-fluffy-switch.rules)
* Save the file to your HOME directory.
* Open terminal and type "ls -l", do you see the file? If not make sure you saved it in the correct location.
* In terminal enter "sudo mv 80-fluffy-switch.rules /etc/udev/rules.d/"
* Restart your computer

### " Error: Permission Denied"
If running Fluffy results in "Permission Denied" error. You may need to set Fluffy.pyw as executable. Run the following command: "sudo chmod +x /path/to/fluffy.pyw"

## Additional MacOS instructions
* brew install libusb <i>(For more info on brew, head to https://brew.sh/)</i>

## Install TinFoil on your Switch
* <b>These steps apply for all custom firmware. This includes but not limited to: Kosmos, ReINX, SXOS, etc.</b>
* Download <a href="https://github.com/fourminute/Fluffy/blob/master/Tinfoil.nro">Recommended TinFoil</a>
* Copy and paste "<b>TinFoil.nro</b>" to a folder named "Switch"(create it if necessary) on the root of your SD card.

## How-To-Use
Complete beginner? No problem. 
* <b>First follow the installation steps above. Done? Let's continue!</b>
* On your Switch running Custom Firmware open TinFoil > Title Management > USB Install NSP
* Double-click on Fluffy.pyw to start it (<b>Linux users: Open Terminal and type "python3 fluffy.pyw".</b>)
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

Answer: You need to make a <a href=https://github.com/fourminute/Fluffy/blob/master/linux/80-fluffy-switch.rules>udev rule</a> to modify the switch usb device owner or group in /etc/udev/rules.d/

<b>Still having problems? Consider making a bug report on this GitHub page to request assistance.</b>

<i>Disclaimer: The "Pink Donut" design was designed by fourminute exclusively for Fluffy and infringes on no copyright. The font used in "intro.png" is also 100% royalty free.</i>
