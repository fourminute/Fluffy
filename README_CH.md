# Fluffy 安装器
![intro](https://github.com/fourminute/Fluffy/blob/master/misc/fluffy-intro.png?raw=true)

### <b><a href="https://github.com/fourminute/Fluffy/releases/latest">下载最新版 Fluffy 安装器</a></b>
### <b><a href="https://github.com/fourminute/Fluffy/blob/master/Tinfoil.nro">下载推荐版本的 TinFoil.nro</a></b>

## 功能
* 支持 <b>XorTroll/Goldleaf</b> 和 <b>Adubbz/Tinfoil</b> 两种NSP游戏文件安装方式。
* 支持USB和网络安装，同时显示传输速率（MB/s）和百分比进程。
* USB和网络安装时，实时显示当前安装的NSP游戏文件。
* 支持Goldleaf（金叶安装器）：显示当前安装的NSP游戏文件。
* 支持Goldleaf（金叶安装器）：显示当前NCA游戏队列。
* 拥有两种传输模式“正常”和“安全”
* 智能生成用户界面，根据安装的模块不同而切换 Tkinter 或者 PyQt(<b>仅支持v1.4.1以上</b>)
* 支持高清显示 4K, 1080P, 和 720P 分辨率。
* 显示当前已经安装的NSP游戏文件。
* 单据NSP游戏文件选择。 (感谢: <b>Shadowhand</b>, thanks!).
* 尝尝甜甜圈（图标）。
* 显示Switch连接状态。
* 5.x USB 修复 (感谢： <a href="https://github.com/satelliteseeker">satelliteseeker</a>)

# 屏幕截图
![screenshot](https://github.com/fourminute/Fluffy/blob/master/misc/screenshot-fluffy-v240c.png?raw=true)


# 使用说明

## 在你的Switch上安装 TinFoil
* <b>以下的操作需要在破解系统上执行。 类似这些破解系统: Kosmos, ReINX, SXOS, etc.</b>
* 下载 <a href="https://github.com/fourminute/Fluffy/blob/master/Tinfoil.nro">推荐版本的 TinFoil</a>
* 复制 "<b>TinFoil.nro</b>" 文件，放到你的SD卡的 "Switch"文件夹中(如果没有需要自己新建)。

## Windows 平台下的使用说明

### 1/3) 安装驱动： Zadig Driver
* 下载 Zadig: https://zadig.akeo.ie 或者备用链接： [github mirror](https://github.com/fourminute/Fluffy/blob/master/windows/zadig-2.4.exe) 。
* 使用USB-C 连接线连接你的Switch和电脑, 在Switch上打开Tinfoil，确认你的Switch已连接电脑并且没有熄屏。
* 打开 Zadig > Options > List All Devices.
* 在下拉选择菜单里选择 "Install Driver",点击箭头切换至 "libusbK".
* 点击 "Install Driver"
* ok啦!

### 2/3) 安装 Python
* 下载并安装好 Python 3  [Python Website](https://www.python.org/downloads/). 安装时候需要勾选 "PATH" option 。
<b>确保之前没有安装过Python 并且不要使用64位的 Python 3. 否则会导致一些错误： "PyUSB not found".</b>

### 3/3) 安装模块库 PyUSB, LibUSB, PyQt5, QDarkStyle
* 打开 Terminal/Command-line/CMD and 输入以下指令:
* pip3 install pyqt5 pyusb libusb libusb1 qdarkstyle
* 无法正常安装请善用百度和谷歌。

### 附加 Windows 安装说明
一些用户反馈了错误： "USB.Core No Backend Available". 如果你也是这个问题请下载 .DLL file [libusb.dll](https://github.com/fourminute/Fluffy/blob/master/windows/libusb-1.0.dll) 并把它和 Fluffy.pyw 放在同一个目录下。

如果你依旧报错, 你可以试试手动安装libusb驱动: [libusb installer](https://github.com/fourminute/Fluffy/blob/master/windows/libusb-win32-devel-filter-1.2.6.0.exe).

## Linux 安装安装说明

### Arch/Manjaro/Antergos
安装 AUR package <a href="https://aur.archlinux.org/packages/fluffy-switch/">fluffy-switch</a> maintained by <a href="https://github.com/YoyPa">YoyPa</a>.

### 其他 安装说明

#### 1/2) 安装 依赖的库文件
* 依赖: ```python3 python3-pyusb python3-pyqt5 libusb libusb1```.
* 可选: ```python3-qdarkstyle```.
* 如果你的包管理器无法帮你安装,可以试试 install ```python3-pip``` 请输入下面的命令（或者善用百度和谷歌）:
* ```pip3 install pyusb pyqt5 libusb libusb1 qdarkstyle```.

#### 2/2) 下载和安装 fluffy 安装器
下载最新的版本 <a href="https://github.com/fourminute/Fluffy/releases/latest">archive</a> , 然后根据以下提示使用:

This is the bare minimum to use fluffy, fluffy itself and a udev rules to change permission on the usb device corresponding to the switch (you might need to reboot to apply udev rule, or at least unplug/plug the switch):
```
mv linux/80-fluffy-switch.rules /etc/udev/rules.d/80-fluffy-switch.rules
mv fluffy.pyw /usr/bin/fluffy
```
Permission are 644 for 80-fluffy-switch.rules and 755 for fluffy:
```
chmod 644 /etc/udev/rules.d/80-fluffy-switch.rules
chmod 755 /usr/bin/fluffy
```

If you want an entry in your launcher and an icon move those files:
```
mv linux/fluffy.desktop /usr/share/applications/fluffy.desktop
mv icons/16x16/fluffy.png /usr/share/icons/hicolor/16x16/apps/fluffy.png
mv icons/24x24/fluffy.png /usr/share/icons/hicolor/24x24/apps/fluffy.png
mv icons/32x32/fluffy.png /usr/share/icons/hicolor/32x32/apps/fluffy.png
mv icons/48x48/fluffy.png /usr/share/icons/hicolor/48x48/apps/fluffy.png
mv icons/64x64/fluffy.png /usr/share/icons/hicolor/64x64/apps/fluffy.png
mv icons/128x128/fluffy.png /usr/share/icons/hicolor/128x128/apps/fluffy.png
```
Permission are 644 for all:
```
chmod 644 /usr/share/applications/fluffy.desktop
chmod 644 /usr/share/icons/hicolor/16x16/apps/fluffy.png
chmod 644 /usr/share/icons/hicolor/24x24/apps/fluffy.png
chmod 644 /usr/share/icons/hicolor/32x32/apps/fluffy.png
chmod 644 /usr/share/icons/hicolor/48x48/apps/fluffy.png
chmod 644 /usr/share/icons/hicolor/64x64/apps/fluffy.png
chmod 644 /usr/share/icons/hicolor/128x128/apps/fluffy.png
```

## MacOS instructions
* brew install libusb <i>(For more info on brew, head to https://brew.sh/)</i>

/!\ This section need to be done /!\

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

