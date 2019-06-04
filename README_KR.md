# Fluffy
![intro](https://github.com/fourminute/Fluffy/blob/master/misc/may_intro_v4.png?raw=true)
 <b><a href="https://github.com/fourminute/Fluffy/blob/master/README.md">Click here for English guide!</a></b>
 <b><a href="https://github.com/fourminute/Fluffy/blob/master/README_CH.md">중국어 안내를 보려면 여기를 클릭하십시오!</a></b>

#### 모든 기부에 감사드립니다! 기부하기로 결정해 주셔서 감사합니다!

<b>Monero</b>:  <sub>4APPsi7nnAs4ZjGC58V5CjVnceEvnZbY1WCBSjmcQsKhGPWLL2EaoUDU2RVFnuLEnASRA2ECXD4YvQ8hyVyZg1raJ482yei</sup>


![License](https://img.shields.io/badge/License-GPLv3-blue.svg) [![Releases](https://img.shields.io/github/downloads/fourminute/fluffy/total.svg)]() [![LatestVer](https://img.shields.io/github/release-pre/fourminute/fluffy.svg)]()

### <b><a href="https://github.com/fourminute/Fluffy/releases/latest">최신 릴리즈 v2.9.0</a></b>
### <b><a href="https://github.com/fourminute/Fluffy/raw/master/Tinfoil.nro">추천하는 TinFoil.nro 다운로드</a></b>
### <b><a href="https://github.com/fourminute/Fluffy/raw/master/Goldleaf.nro">추천하는 Goldleaf.nro 다운로드</a></b>


## 기능
* <b>XorTroll/Goldleaf</b> 과 <b>Adubbz/Tinfoil</b> 지원
* 언어 지원: <b>영어, 중국어, 베트남어, 스페인어, 프랑스어, 브라질 포르투갈어,터키어, 이탈리아어, 독일어, 인도네시아어</b>!
* 크로스 플랫폼: <b>Windows</b>, <b>Linux</b>, <b>MacOS</b>에서 실제로 솜털 같은 구동!
* USB 와 네트워크: 진행률과 함께 라이브 전송률을 MB/s 단위로 표시.
* USB 와 네트워크: 현재 NSP가 설치되고 번호가 매겨진 대기열을 표시.
* USB 와 네트워크: 개별 선택으로 배치 NSP 설치 지원.
* USB 와 네트워크: 다시 시작하지 않고 연속 설치. 
* USB 와 네트워크: 예외/오류 처리, 설치 실패시 다시 시작하지 않음.
* USB 와 네트워크: 대기열에 있는 설치를 중단하는 기능.
* Tinfoil 네트워크: Tinfoil 코드의 길이 파일 이름 버그를 수정하기 위한 파일 URL 도용.
* Tinfoil 네트워크: 랜덤 포트 선택.
* Tinfoil 네트워크: 기본적으로 USB 모드를 사용할 수 없는 경우 네트워크 모드로 폴백 (예: 누락된 라이브러리).
* Goldleaf: 현재 접속중인 파일 표시.
* Goldleaf: Goldleaf v0.6은 모든 파일 처리 기능과 호환.
* Goldleaf: 잠재적으로 손상된 Goldleaf 파일로부터 사용자를 안전하게 지키기위한 기본 보호 기능.
	* 기본값: 파일 생성, 삭제, 이름 변경과 같은 파일 조작은 사용자 프롬프트 (예 또는 아니오) 표시.
	* 기본값: 모든 파일에 대한 읽기 전용 접속.
	* 기본값: NSP가 아닌 파일에 대한 읽기/쓰기 제한
	* 이러한 보안 제한은 모두 fluffy.conf에서 변경할 수 있음.
* Tinfoil USB: 노후화 된 하드웨어(예: USB 포트 스펙에 벗어남)의 경우 "정상 모드"와 "안전 모드" 사이의 선택 가능한 전송 속도.
* USB: 스위치 인디게이터 연결.
* 사용자 인터페이스: 밝은 모드와 어두운 모드.
* 일반: 스위치 IP 주소, 밝음/어두움 모드 설정, 언어 선택 구성 자동 저장.
* 최대 4K 해상도의 UI 확장에 대한 일반 지원.
* Tinfoil USB: 스위치 펌웨어 5.x USB 수정 (이것을 수정한 <a href="https://github.com/satelliteseeker">satelliteseeker</a>에게 감사드립니다. '안전 모드'를 선택하세요.)
* 귀여운 솜털로 뒤덮인 펭귄.

# 스크린샷

<img src="https://github.com/fourminute/Fluffy/blob/master/misc/uifluffy-sq3.png?raw=true" width="800"/>

# [윈도우] 사용 지침서 (Fluffy.exe)

## 1/3) 스위치에 TinFoil 또는 Goldleaf 설치
* <b>이 단계는 모든 사용자 정의 펌웨어에 적용됩니다. 여기에는 다음이 포함되지만 이에 국한되지 않습니다: Kosmos, ReINX, SXOS 등.</b>
* <a href="https://github.com/fourminute/Fluffy/blob/master/Tinfoil.nro">추천하는 TinFoil</a> 다운로드
* "<b>TinFoil.nro</b>" t를 복사하여 SD 카드의 루트에 "Switch"라는 폴더에 복사하십시오 (필요한 경우 생성하십시오).
* <i>또는</i>  XorTroll의 <a href="https://github.com/XorTroll/Goldleaf/releases">Goldleaf</a> 다운로드.

### 2/3) Zadig 드라이버 설치 및 설정
* Zadig 다운로드: https://zadig.akeo.ie 또는 웹 사이트가 다운 될 경우 [github 미러](https://github.com/fourminute/Fluffy/blob/master/windows/zadig-2.4.exe)
* (스위치에서) USB-C 케이블을 사용하여 스위치를 PC에 연결한 상태에서 TinFoil을 엽니다. 이렇게하면 스위치가 보이도록 할 수 있습니다.
* Zadig 열기 > 옵션 > 모든 장치 나열
* "드라이버 설치" 버튼 위의 스크롤 상자에서 "libusbK"에 도달할 때까지 화살표를 탭 합니다.
* "드라이버 설치" 클릭
* 완료!

### 3/3) Fluffy 실행 및 NSP 설치! (Tinfoil)
* 스위치와 PC를 USB Type-C 케이블로 연결
* Fluffy.exe 실행
* 스위치 Tinfoil 열기 > 타이틀 관리자 > USB 설치 NSP
* Fluffy에서 "NSP 선택" > NSP 선택하여 클릭
* Fluffy의 Tinfoil USB 화면 "전송 시작" 클릭

### 3/3) Fluffy 실행 및 NSP 설치! (Goldleaf)
* Fluffy.exe 실행
* 스위치에서 Goldleaf 열기 > 컨텐츠 탐색
* Fluffy의 Goldleaf 화면 "전송 시작" 클릭
* 스위치에서 "(USB를 통해) PC 드라이브" 선택
* NSP로 이동하여 설치

# [윈도우] 사용 지침서 (Fluffy.pyw)

## 1/5) 스위치에 TinFoil 또는 Goldleaf 설치
* <b>이 단계는 모든 사용자 정의 펌웨어에 적용됩니다. 여기에는 다음이 포함되지만 이에 국한되지 않습니다: Kosmos, ReINX, SXOS, 등.</b>
* <a href="https://github.com/fourminute/Fluffy/blob/master/Tinfoil.nro">추천하는 TinFoil</a> 다운로드
* "<b>TinFoil.nro</b>" 를 복사하여 SD 카드의 루트에 "Switch"라는 폴더에 복사하십시오 (필요한 경우 생성하십시오).
* <i>or</i>  XorTroll의 <a href="https://github.com/XorTroll/Goldleaf/releases">Goldleaf</a> 다운로드.

### 2/5) Zadig 드라이버 설치 및 설정
* Zadig 다운로드: https://zadig.akeo.ie 또는 웹 사이트가 다운 될 경우 [github 미러](https://github.com/fourminute/Fluffy/blob/master/windows/zadig-2.4.exe)
* (스위치에서) USB-C 케이블을 사용하여 스위치를 PC에 연결한 상태에서 TinFoil을 엽니다. 이렇게하면 스위치가 보이도록 할 수 있습니다.
* Zadig 열기 > 옵션 > 모든 장치 나열
* "드라이버 설치" 버튼 위의 스크롤 상자에서 "libusbK"에 도달할 때까지 화살표를 탭 합니다.
* "드라이버 설치" 클릭
* 완료!

### 3/5) 파이썬 설치
* [파이썬 웹사이트](https://www.python.org/downloads/) 에서 파이썬 3을 다운로드하여 설치하십시오. 설치 중에 "PATH"옵션을 선택하십시오. <b>이전 버전의 파이썬이 설치되어 있지 않은지 확인하고 64 비트 버전의 파이썬 3을 사용하지 마십시오. 이로 인해 "PyUSB not found" 오류가 발생할 수 있습니다.</b> 또한 설치시 Tkinter를 포함시켜야 합니다 (기본 옵션이어야 함).

### 4/5) 파이썬 종속성 설치
* 명령줄/CMD (시작, 검색 "CMD")를 열고 다음을 실행:
```
pip3 install pyusb pyqt5 libusb libusb1 qdarkstyle configparser
```

### 5/5) Fluffy 실행 및 NSP 설치! (Tinfoil)
* 스위치와 PC를 USB Type-C 케이블로 연결
* Fluffy.pyw 실행
* 스위치에서 Tinfoil 열기> 타이틀 관리자 > USB 설치 NSP
* Fluffy에서 "NSP 선택" > NSP 선택 클릭
* Fluffy의 Tinfoil USB 화면 "전송 시작" 클릭

### 5/5) Fluffy 실행 및 NSP 설치! (Goldleaf)
* 스위치와 PC를 USB Type-C 케이블로 연결
* Fluffy.pyw 실행
* 스위치에서 Goldleaf 열기 > 컨텐츠 탐색
* Fluffy의 Goldleaf 화면 "전송 시작" 클릭
* 스위치에서 "(USB를 통해) PC 드라이브"를 선택
* NSP로 이동하여 설치

## 리눅스 지침서

### 우분투/데비안 기반 배포판

#### 1/3) 파이썬과 종속성 설치
* 요구사항: ```python3 python3-pyusb python3-pyqt5 python3-tk python3.6-tk libusb libusb1 qdarkstyle```.
* 파이썬3 설치:
* ```sudo apt install python3 python3-pip python3-tk```.
* 그런 다음 터미널을 열고이 명령을 실행하십시오:
* ```pip3 install pyusb pyqt5 libusb libusb1 qdarkstyle configparser```.
* 작동하지 않는 경우 시도하십시오.y
* ```pip install pyusb pyqt5 libusb libusb1 qdarkstyle configparser```.

#### 2/3) Fluffy 와 Switch Rule 다운로드
최신 <a href="https://github.com/fourminute/Fluffy/releases/latest">Fluffy.pyw</a> 와 <a href="https://github.com/fourminute/Fluffy/blob/master/linux/80-fluffy-switch.rules">80-fluffy-switch.rules</a>를 다운로드 합니다.

터미널을 열고 cd 명령을 사용하여이 파일들이 있는 디렉토리로 변경하십시오:
 ```
 cd /path/to/fluffy/
 ```
 
이 명령을 사용하여 <b>80-fluffy-switch.rules</b> 파일을 <b>/etc/udev/rules.d/</b>에 복사합니다:
```
sudo cp 80-fluffy-switch.rules /etc/udev/rules.d/
```
그런 다음 적절한 권한을 부여하십시오:
```
sudo chmod 644 /etc/udev/rules.d/80-fluffy-switch.rules
sudo chmod 755 fluffy.pyw
```
#### 3/3) Fluffy 시작
Fluffy.pyw를 시작하려면 두 번 클릭하여 열 수 있어야 합니다. 하지만 그게 작동하지 않으면 터미널을 사용하여 Fluffy.pyw를 실행해야 할 수도 있습니다. IDLE(파이썬 인터페이스)을 설치할 수 있습니다.

터미널 열기 및 입력:
```
python3 /path/to/fluffy.pyw
```
<i>다른 방법으로</i>,  IDLE(파이썬 인터페이스)을 설치할 수 있습니다.
```
sudo apt-get install idle3
```
IDLE 열기 > Fluffy.py를 열고 실행 > 모듈 실행을 선택하십시오.

### Arch/Manjaro/Antergos
<a href="https://github.com/YoyPa">YoyPa</a>가 유지관리하는 <a href="https://aur.archlinux.org/packages/fluffy-switch/">fluffy-switch</a> AUR 패키지 설치.

### 설치 및 응용 프로그램 시작 관리자 (선택 사항)
Fluffy 설치를 원할 수 있습니다. Download the latest <a href="https://github.com/fourminute/Fluffy/releases/latest">Fluffy.pyw</a> and 'icon.ico' and 'install.sh' from <a href="https://github.com/fourminute/Fluffy/tree/master/linux">여기에서</a> 최신 <a href="https://github.com/fourminute/Fluffy/releases/latest">Fluffy.pyw</a>와 'icon.ico'와 'install.sh'를 다운로드하십시오. 압축을 풀고 각 파일을 단일 폴더로 이동하십시오.

설치는 다음과 같이 간단합니다:
```
cd /path/to/files/
sudo ./install.sh
```
## MacOS 지침서
```
brew install tcl-tk
brew reinstall python3
pip3 install pyusb pyqt5 libusb libusb1 qdarkstyle configparser
python3 ./fluffy.pyw
```
<sub>이 지침에 대한 <a href="https://github.com/GuillaumeJulien">GuillaumeJulien</a>에게 특별히 감사드립니다.</sup>

<sub><i>brew에 대한 자세한 내용은 https://brew.sh/ 를 방문하십시오.</i></sup>


## 문제해결 팁
<b>(리눅스)Fluffy.pyw는 여전히 미확인 파일로 나타납니까?</b>

답변: 터미널을 사용하여 실행
```
python3 fluffy.pyw
```

<b>왜 "USBCore No Backend Available" 오류가 계속 발생합니까?</b>

답변: 이것은 1-2 가지로 인해 발생할 수 있습니다.

1) <a href="https://github.com/fourminute/Fluffy/raw/master/windows/libusb-1.0.dll">libusb-1.0.dll</a>을 다운로드하여 Fluffy 폴더에 넣으십시오. 그래도 문제가 해결되지 않으면 Zadig 또는 <a href="https://github.com/fourminute/Fluffy/raw/master/windows/libusb-win32-devel-filter-1.2.6.0.exe">libusb-win32-devel-filter 설치 프로그램</a>을 사용하여 LibUSB를 설치하십시오.

2) 모든 USB Type-C 케이블이 스위치에서 작동하는 것은 아닙니다. 스위치가 연결되면 자주 연결을 끊은 다음 다시 연결하십시오. 또는 이 오류가 발생하면 최신 USB Type-C 케이블이 필요할 것입니다. 예, 시각적으로 유사함에도 불구하고 차이가 있습니다.

<b>계속 오류가 발생하는 이유는 무엇입니까?: "No module named 'PyQt5'"?</b>

파이썬을 설치할 때 "PATH"가 선택되었는지 확인하십시오. 그래도 해결되지 않으면 IDLE(32 비트 모드)을 사용하여 Fluffy를 실행 해 보십시오.

<b>네트워크가 멈추거나 정지되는 이유는 무엇입니까?</b>

답변: 이것은 정상입니다. 네트워크 설치가 잠시 중단 될 수 있으며 네트워크, 와이파이를 사용하는 장비 수, 와이파이 속도 등에 따라 작업 시간이 오래 걸릴 수 있습니다. 전송을 시작하면 시간이 좀 걸릴 수 있습니다. 몇 분이 걸릴 수 있습니다.  Fluffy은 얼어 붙은 것처럼 보일 수 있지만 대부분의 경우 약간의 인내가 권장됩니다.

<b>스위치는 어떤 종류의 케이블을 사용합니까?</b>

답변: USB Type-C 케이블. 하지만 모든 USB Type-C 케이블이 동일하지는 않습니다. 일부는 스위치와 호환되지 않습니다.

<b>MacOS와 Linux에서 Fluffy가 작동합니까?</b>

답변: 당연합니다! 파이썬은 크로스 플랫폼이므로 Fluffy는 두 운영 체제 모두에서 작동해야합니다.

<b>Fluffy 및 TinFoil에서 가장 적합한 사용자 정의 펌웨어는 무엇입니까?</b>

답변: 그들 모두는 똑같이 작동 할 것입니다. 그건 당신에게 달렸습니다.

<b>왜 내 설치가 멈추거나 계속 충돌합니까?</b>

답변: 전송 모드를 "안전 모드"로 전환하십시오. Tinfoil 네트워크를 통해 설치하는 경우 설치가 중단되는 것이 일반적입니다.

<b>불충분한 권한 오류 (usb)(Linux)가 있는 이유는 무엇입니까? (크레딧: YoyPa)</b>

답변: /etc/udev/rules.d/에서 스위치 USB 장치 권한을 수정하려면 <a href=https://github.com/fourminute/Fluffy/blob/master/linux/80-fluffy-switch.rules>udev rule</a>을 만들어야합니다.

<b>여전히 문제가 있습니까? 도움을 요청하려면 이 GitHub 페이지에서 버그 보고서를 작성하십시오.</b>


## 크레딧

Fluffy는 처음부터 끝까지 모든 기능과 버그 수정을 포함하여 Fourminute에 의해 개발되었지만 Fluffy 개선에 많은 시간과 노력을 기울여 온 사람들이 있습니다.

Fluffy는 오늘날 도움을 주신 아래 사람들에게 감사 드리고 싶습니다.

* <a href="https://github.com/wendyliga">wendyliga</a> 인도네시아어 번역.
* <a href="https://github.com/TheLastZombie">TheLastZombie</a> 독일어 번역.
* <a href="https://github.com/YoyPa">YoyPa</a> 그들의 많은 다양한 코드 공헌을 위해 <a href="https://aur.archlinux.org/packages/fluffy-switch/">fluffy-switch</a> AUR 패키지와 스페인어 프랑스어 번역.
* LoOkYe, MacOS에서 Fluffy의 다양한 개발 단계에서 테스트 및 디버깅. 단계
* <a href="https://github.com/friedkeenan">friedkeenan</a> Goldleaf v0.6 호환성에 대한 엄청난 도움을 얻었습니다.
* <a href="https://github.com/TorpedoXL">TorpedoXL</a> 터키어 번역.
* <a href="https://github.com/DavidOliM">DavidOliM</a> 브라질 포르투갈어 번역.
* <a href="https://github.com/danypava">danypava</a> 이탈리아어 번역.
* <a href="https://github.com/Sev73n">Sev73n</a> 중국어(북경어) 번역은 물론 README 전체를 번역.

내가 놓친 다른 사람들에게도 고맙습니다.

<i>"귀여운 펭귄"은 fourminute에 의해 디자인 되었습니다.
"Fluffy" 로고에 사용된 글꼴은 100% 로열티가 없습니다.

Fluffy(이 프로그램)과 "귀여운 펭귄" 
디자인은 (c) 2019 fourminute의 Copyright 입니다.
(https://github.com/fourminute)</i>
