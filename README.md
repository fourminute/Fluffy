# Fluffy
A one-dependency, feature-rich GUI for Tinfoil!

### <b><a href="https://github.com/fourminute/Fluffy/releases/tag/v1.2">Latest Release v1.2</a></b>
### <b><a href="https://github.com/fourminute/Fluffy/blob/master/Tinfoil.nro">Download Recommended TinFoil.nro</a></b>

## Features
* Show current NSP being installed.
* Individual NSP selection.
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

## Install Python and PyUSB
* <b>Fluffy requires <u>ONLY the latest</u> Python 3 and PyUSB.</b>
* Download and Install Python 3 from https://www.python.org/downloads/. <b>Ensure no previous version of Python is installed. This may cause an error "PyUSB not found".</b>
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

## Troubleshooting Tips
<b>PyUSB Not Found and I've followed all the steps!</b>

Answer: Ensure no previous versions of Python are installed. If necessary, uninstall them. For example, if you have Python 3.6.6 and Python 3.7.2 installed at the same time Fluffy may throw this error.

<b>What kind of cable does the Switch use?</b>

Answer: USB type C cable.

<b>Does Fluffy work on MacOS and Linux?</b>

Answer: Absolutely! Python is cross-platform and so Fluffy should work on both operating systems.

<b>Which Custom Firmware works best with Fluffy and TinFoil</b>

Answer: All of them will work the same. That is up to you.


<b>Still having problems? Consider making a bug report on this GitHub page to request assistance.</b>
