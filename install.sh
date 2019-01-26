#!/bin/sh
INIT_DIR=`pwd`
echo "Installing Fluffy."
echo "Installing Python3."
sudo apt install python3
echo "Installing Python3-pip."
sudo apt install python3-pip
echo "Installing pip dependencies."
pip3 install pyusb
pip3 install pyqt5
pip3 install libusb
pip3 install libusb1
echo "Saving desktop icon."
sudo echo "[Desktop Entry]
Type=Application
Terminal=false
Name=Fluffy
Exec=python3 $INIT_DIR/fluffy.pyw
Icon=$INIT_DIR/icon.ico
StartupWMClass=Fluffy" > /usr/share/applications/fluffy-desktop.desktop
echo "Setting up Switch rules."
sudo echo "SUBSYSTEMS==\"usb\", ATTR{idVendor}==\"057e\", MODE=\"0666\"" > /etc/udev/rules.d/80-fluffy-switch.rules
sudo chmod u+x /usr/share/applications/fluffy-desktop.desktop
echo "Fluffy Installed Successfully."
echo "Please restart your computer for Switch USB ruleset to take effect."
