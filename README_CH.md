# Fluffy 安装器
![intro](https://github.com/fourminute/Fluffy/blob/master/misc/may_intro_v4.png?raw=true)

### <b><a href="https://github.com/fourminute/Fluffy/releases/latest">下载最新版 Fluffy 安装器</a></b>
### <b><a href="https://github.com/fourminute/Fluffy/blob/master/Tinfoil.nro">下载推荐版本的 TinFoil.nro</a></b>

## 功能
* 支持 <b>XorTroll/Goldleaf</b> 和 <b>Adubbz/Tinfoil</b> 两种NSP游戏文件安装方式。
* 支持<b>英文！简体中文，法语，意大利语和越南语等多种语言！并不断更新中。</b>
* 支持USB和网络安装，同时显示传输速率（MB/s）和百分比进程。
* USB和网络安装时，实时显示当前安装的NSP游戏文件。
* 支持Goldleaf（金叶安装器）：显示当前安装的NSP游戏文件。
* 拥有两种传输模式“正常”和“安全”
* 支持高清显示 4K, 1080P, 和 720P 分辨率。
* 显示当前已经安装的NSP游戏文件。
* 单据NSP游戏文件选择。
* 尝尝甜甜圈（图标）。
* 显示Switch连接状态。
* 5.x USB 修复 

# 屏幕截图
<img src="https://github.com/fourminute/Fluffy/blob/master/misc/uifluffy-sq3.png?raw=true" width="800"/>


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

## Linux 安装说明

### Arch/Manjaro/Antergos
安装 AUR package <a href="https://aur.archlinux.org/packages/fluffy-switch/">fluffy-switch</a> 来自 <a href="https://github.com/YoyPa">YoyPa</a>.

### 其他 安装说明

#### 1/2) 安装 依赖的库文件
* 依赖: ```python3 python3-pyusb python3-pyqt5 libusb libusb1```.
* 可选: ```python3-qdarkstyle```.
* 如果你的包管理器无法帮你安装,可以试试 install ```python3-pip``` 请输入下面的命令（或者善用百度和谷歌）:
* ```pip3 install pyusb pyqt5 libusb libusb1 qdarkstyle```.

#### 2/2) 下载和安装 fluffy 安装器
下载最新的版本 <a href="https://github.com/fourminute/Fluffy/releases/latest">安装包</a> , 然后根据以下提示使用:

这只是最简单使用fluffy的方式，如果遇到问题，你可以试试重启电脑或者重新插拔一下Switch以应用驱动，或者试试手动给fluffy赋予权限:
```
mv linux/80-fluffy-switch.rules /etc/udev/rules.d/80-fluffy-switch.rules
mv fluffy.pyw /usr/bin/fluffy
```
权限说明： 644 for 80-fluffy-switch.rules and 755 for fluffy:
```
chmod 644 /etc/udev/rules.d/80-fluffy-switch.rules
chmod 755 /usr/bin/fluffy
```

如果你需要在lanucher里面显示图标，请尝试以下命令:
```
mv linux/fluffy.desktop /usr/share/applications/fluffy.desktop
mv icons/16x16/fluffy.png /usr/share/icons/hicolor/16x16/apps/fluffy.png
mv icons/24x24/fluffy.png /usr/share/icons/hicolor/24x24/apps/fluffy.png
mv icons/32x32/fluffy.png /usr/share/icons/hicolor/32x32/apps/fluffy.png
mv icons/48x48/fluffy.png /usr/share/icons/hicolor/48x48/apps/fluffy.png
mv icons/64x64/fluffy.png /usr/share/icons/hicolor/64x64/apps/fluffy.png
mv icons/128x128/fluffy.png /usr/share/icons/hicolor/128x128/apps/fluffy.png
```
权限都是 664:
```
chmod 644 /usr/share/applications/fluffy.desktop
chmod 644 /usr/share/icons/hicolor/16x16/apps/fluffy.png
chmod 644 /usr/share/icons/hicolor/24x24/apps/fluffy.png
chmod 644 /usr/share/icons/hicolor/32x32/apps/fluffy.png
chmod 644 /usr/share/icons/hicolor/48x48/apps/fluffy.png
chmod 644 /usr/share/icons/hicolor/64x64/apps/fluffy.png
chmod 644 /usr/share/icons/hicolor/128x128/apps/fluffy.png
```

## MacOS 安装说明
* 在终端里执行：brew install libusb <i>(关于 brew, 点这 https://brew.sh/)</i>

/!\ 有了brew的MacOS很方便！这就行了 /!\

## 如何使用
完全是新手？也没关系。 
* <b>完成了上面的安装说明了？OK！让我们继续吧！</b>
* 在你的Switch上打开破解系统，一般进入的操作是进入相册，然后找到 TinFoil > Title Management > USB Install NSP.
* 双击 Fluffy.pyw 文件 (Linux 用户:在你的开始菜单或者 terminal里输入 ```fluffy```).
* 点击 "选择 NSP 游戏文件" 选择你想安装的游戏文件，可以选择多个哦.
* 如果显示 "Switch 已连接!" 。点击 "开始传输"。
* 在你的Switch的 TinFoil 上, 选择要安装的游戏文件.

## 遇到小问题了？
<b>报错 : "USBCore No Backend Available"?</b>

 这可能有以下两点引起的：

1) 你的USB-C线不支持，试试换一条更好的。

2) LibUSB 驱动没有成功安装. 通过以下命令安装 "pip3 install libusb" 和 "pip3 install libusb1"。

<b>一直提示: "No module named 'PyQt5'"?</b>

首先，Fluffy不支持64位的Python，请使用32位的Python运行.


<b>网络安装出错?</b>

检查或关闭防火墙，特别是 2000 端口要打开. 确保你的Switch和电脑在同一个局域网中。

<b>PyUSB Not Found</b>

注意：**Fluffy不支持64位的Python，请使用32位的Python运行。** 或试着删除之前的Python版本，注意只保留32位的Python3就可以。

<b>我需要什么类型的数据线?</b>

USB type C 数据线就可以。注意也不是所以的USB-C的线都能够完美支持。

<b>MacOS 和 Linux 可以运行 Fluffy 吗?</b>

当然啦！Python是跨平台的，所以 Fluffy 也可以的！

<b>哪种破解系统最适合运行 Fluffy 和 TinFoil?</b>

大部分都可以，看你喜欢用哪个，译者用的是大气层。

<b>为什么我安装的时候总是程序崩溃?</b>

不如试试“安全模式”？

<b>提示错误： unsufficient permission error (usb)(linux)? (credit: YoyPa)</b>

将 <a href=https://github.com/fourminute/Fluffy/blob/master/linux/80-fluffy-switch.rules>udev rule</a> 放到你的系统驱动配置 /etc/udev/rules.d/ 中。

<b>如果还有其他问题，可以issue这个Github主页，期待你让 Fluffy 变得更好。</b>

