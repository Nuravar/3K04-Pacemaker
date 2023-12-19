# Pace++ 💖
Pace++ is a simulated pacemaker built to visually and functionally represent the various functions of modern pacemakers today. The following project is based of [Boston Scientific's](https://www.bostonscientific.com/en-US/Home.html) pacemaker specifications. 

Through model-based code generation and a python gui, we created the following features:
- 7 unique pacemaker modes (AOO, VOO, AAI, VVI, AOOR, VOOR, AAIR, VVIR)
- Real-time electrocardiogram display
- Local encrypted data storages     

## Technology Stack
[Python](https://www.python.org/) | [Matlab Simulink](https://www.mathworks.com/products/simulink.html) | [Customtkinter](https://customtkinter.tomschimansky.com/) | [NXP FRDM K64F Board](https://www.nxp.com/design/design-center/development-boards/freedom-development-boards/mcu-boards/freedom-development-platform-for-kinetis-k64-k63-and-k24-mcus:FRDM-K64F) | [J-Link](https://www.segger.com/downloads/jlink/)

## Showcase 
#### DCM
<p align="center">
  <img src="Images/IntroScreen-Dark.png" alt="Intro Screen Dark" />
  <br>
  <em>The Intro Screen in Dark Mode</em>
</p>
<p align="center">
  <img src="Images/IntroScreen-Light.png" alt="Intro Screen Dark" />
  <br>
  <em>The Intro Screen in Dark Mode</em>
</p>

<p align="center">
  <img src="Images\EgramScreen1.png" alt="Intro Screen Dark" />
  <br>
  <em>Display of Heartrate in Dark Mode</em>
</p>

#### Simulink
<p align="center">
  <img src="Images\Simulink1.jpg" alt="Intro Screen Dark" />
  <br>
  <em>General Overview of the Simulink Stateflow</em>
</p>
<p align="center">
  <img src="Images\Simulink3.jpg" alt="Intro Screen Dark" />
  <br>
  <em> Overview of the Parameter Processing</em>
</p>
<p align="center">
  <img src="Images\Simulink2.jpg" alt="Intro Screen Dark" />
  <br>
  <em>Overview of the Pacemaker Modes</em>
</p>


## Development Process
#### Modeling with MATLAB Simulink
Central to modelling our pacemaker's functionality was the use of MATLAB Simulink, which allowed us to generate code iteratively and quickly flash our code into our board. 

Through user-set parameters, our Simulink code allow for pacing of both the atrium and ventricle alongside rate adaptive pacing with a in-built accelerometer. 

All important user-set data and electrocardiogram data was framed. The resulting packet was sent through a micro-usb to the device controller monitor.  
#### Device Controller Monitor (DCM)
Through python's tkinter, we created a secure interface that allows for the modification of the pacemaker. Our GUI allows for:
- Real-time display of the simulated heartbeat
- Patient data to be saved and modified
- Encryption of patient data
- Serial communication to the K64F board

#### Validation
To test and validate our pacemaker mode function, we employed Heartview, a McMaster created cardiac simulation tool that was pre-flashed onto our board.

## Installation
#### Prerequisites
1. Python 3.18 or later
2. MATLAB Simulink 2023 or later

#### Python Libraries 
```bash
pip install customtkinter matplotlib serial cyrptography 
```

#### MATLAB Simulink Libraries
- Embedded Coder, Fixed-Point Designer, MATLAB Coder, Simulink Check, Simulink Coder, Simulink Coverage, Simulink Design Verifier, Simulink Desktop Real-Time, Simulink Test, and Stateflow
- [Simulink Coder Support Package for NXP FRDM-K64F Board](https://www.mathworks.com/matlabcentral/fileexchange/55318-simulink-coder-support-package-for-nxp-frdm-k64f-board#:~:text=Simulink%C2%AE%20Coder%E2%84%A2%20Support,K64F%20peripherals%20and%20communication%20interfaces.)
- [Kinetis SDK 1.2.0 mainline release](https://www.nxp.com/design/design-center/designs/software-development-kit-for-kinetis-mcus:KINETIS-SDK)
- [V6.20a of the J-Link Software](https://www.segger.com/downloads/jlink/)

In MATLAB, write the following in to the terminal:
```matlab
open([codertarget.freedomk64f.internal.getSpPkgRootDir,
'/src/mw_sdk_interface.c']);
```
Upon opening the device change the following line:
```matlab
{ GPIO_MAKE_PIN(GPIOA_IDX, 0),  MW_NOT_USED},// PTA0, D8
```
into the following:
```matlab
{ GPIO_MAKE_PIN(GPIOC_IDX, 12),  MW_NOT_USED},// PTC12, D8
```

## Contributors
[Christopher Nazarian](https://www.linkedin.com/in/christopher-nazarian-66394016a/)
[Himanshu Singh](https://www.linkedin.com/in/himanshu-singh-99470b207/)
[Matthew Galuszka](https://www.linkedin.com/in/mathew-galuszka-151bb1231/)
[Shaan Suthar](https://www.linkedin.com/in/shaan-suthar/)
[Varun Kothandaraman](https://www.linkedin.com/in/varun-ram/)
[Shivan Guar](https://www.linkedin.com/in/shivan-gaur/)




