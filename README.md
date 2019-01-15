# Fluffy
A one-dependency, feature-rich GUI for Tinfoil!

### <b><a href="https://github.com/fourminute/Fluffy/releases/tag/v1.1">Latest Release</a></b>
### <b><a href="https://github.com/fourminute/Fluffy/blob/master/Tinfoil.nro">Download Recommended TinFoil.nro</a></b>

## Features
* Show current NSP being installed.
* Progress bar.
* Switch connected indicator.
* 5.x USB Fix (Thanks to <a href="https://github.com/satelliteseeker">satelliteseeker</a>)

<img src="https://i.imgur.com/oGuVBHQ.png" />

## Coming soon
<b>High-priority</b>
* GoldLeaf Support (<i>on top</i> of existing TinFoil support)

<b>Low/Medium-priority:</b>
* Network Installs for TinFoil

# Instructions For Use
## Install and Setup Zadig Driver (Windows 10)
* Download Zadig: https://zadig.akeo.ie.
* With your Switch plugged in to your PC using a USB-C cable, open TinFoil(on your Switch). This will ensure your Switch is visible.
* Open Zadig > Options > List All Devices.
* In the scroll box above the button "Install Driver", tap the arrow until arriving at "libusbK".
* Click "Install Driver"
* Done!

## Install PyUSB
* <b>Python 3 and PyUSB is required for Fluffy to work.</b>
* Download and Install Latest Python 3 (https://www.python.org/downloads/)
* Open Terminal/CMD
* Run "pip3 install pyusb"
* <i>MacOS users must also run "brew install libusb". For more info on brew, head to https://brew.sh/.</i>

## Install TinFoil
* <b>These steps apply for all custom firmware. This includes but not limited to: Kosmos, ReINX, SXOS, etc.</b>
* Download <a href="https://github.com/fourminute/Fluffy/blob/master/Tinfoil.nro">Recommended TinFoil</a>
* Copy and paste "<b>TinFoil.nro</b>" to a folder named "Switch"(create it if necessary) on the root of your SD card.

## How-To-Use
Complete beginner? No problem. 
* <b>First follow the installation steps above for Zadig Driver, TinFoil, Python 3, and PyUSB. Done? Let's continue!</b>
* On your Switch running Custom Firmware open TinFoil > Title Management > USB Install NSP
* Double-click on Fluffy.pyw to start it
* Click "Open Folder" and browse to a folder where your NSPs are located then select "Open". <b>A word of caution, try to select a folder with 3 or less NSPs. TinFoil is unable to parse large amounts of files.</b>
* If "Switch Detected!" is visible. Click "Send Header".
