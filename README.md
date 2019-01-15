# Fluffy
A one-dependency, feature-rich GUI for Tinfoil!

## Features
* Show current NSP being installed.
* Progress bar.
* Switch connected indicator.
* 5.x USB Fix (Thanks to <a href="https://github.com/satelliteseeker">satelliteseeker</a>)

<img src="https://i.imgur.com/kOLaqQx.png" />

## Coming soon
<b>High-priority</b>
* Better UI multi-threading (Tk by default, is not thread safe. Hacky-methods are necessary)
* Code optimization and fail-safes.
* (<i>If necessary</i>) NCA Buffering. See <a href="https://github.com/satelliteseeker/Tinfoil/commit/f33c735e3fda9e8127ec3b3b5f7296a438dc9a2c">f33c735</a>.

<b>Medium-priority:</b>

* GoldLeaf Support (<i>on top</i> of existing TinFoil support)

<b>Low-priority:</b>

* Network Installs for TinFoil

# Instructions For Use
## Install and Setup Zadig Driver (Windows 10)
* Download and Install Zadig: https://zadig.akeo.ie.
* <b>While your Switch is plugged in</b> head to Device Manager.
* Under "Other Devices" find "libnx USB comms", right-click it and click "Update driver".
* Click "Browse my computer..." then "Let me pick from a list..."
* Find and select "libusbK USB Devices" then click next.
* With "Nintendo Switch APX Mode" selected click next.
* Click <b>Yes</b> to any warning pop-up messages.
* Done!

## Install PyUSB
* <b>Python 3 and PyUSB is required for Fluffy to work.</b>
* Download and Install Latest Python 3 (https://www.python.org/downloads/)
* Open Terminal/CMD
* Run "pip3 install pyusb"
* <i>MacOS users must also run "brew install libusb". For more info on brew, head to https://brew.sh/.</i>

## How-To-Use
Complete beginner? No problem. 
* <b>First follow the installation steps above for Zadig Driver, Python 3, and PyUSB. Done? Let's continue!</b>
* On your Switch running Custom Firmware open TinFoil > Title Management > USB Install NSP
* Double-click on Fluffy.py to start it
* Click "Open Folder" and browse to a folder where your NSPs are located then select "Open". <b>A word of caution, try to select a folder with 3 or less NSPs. TinFoil is unable to parse large amounts of files.</b>
* If "Switch Detected!" is visible. Click "Send Header".
