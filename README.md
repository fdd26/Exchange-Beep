Works with Python 3.12+    
    
Tested successfully on Windows Desktop    
    
    
Windows 7 / 10 / 11 instructions    
================================    
    
GO HERE:    
--------    
  https://www.python.org/downloads/    
    
DOWNLOAD THIS:    
--------------    
  https://www.python.org/ftp/python/3.12.2/python-3.12.2-amd64.exe    
    
  [x] Install Python3 for all users    
  [x] Add Python3 to your PATH environment    
    
DOWNLOAD THIS:    
--------------    
  https://codeload.github.com/fdd26/Exchange-Beep/zip/refs/heads/main?file=Exchange-Beep-main.zip    
    
Extract it    
----------    
    
OPEN cmd.exe in that folder    
    
TYPE THIS to install Python3 dependencies:    
------------------------------------------    
  ```sh    
  pip3 install pyautogui    
  pip3 install python_imagesearch    
  ```    
    
TYPE THIS to run the program    
----------------------------    
  ```sh    
  python.exe Main.py    
  ```    
    
OR double-click on Main.py    
    
OPEN exchange.png to test, you should hear some beeps.    
    
    
    
MAC OS X instructions    
=====================    
    
Download Mac OS Python 3.12.x    
https://www.python.org/downloads/macos/    
    
https://www.python.org/ftp/python/3.12.4/python-3.12.4-macos11.pkg    
    
Download and Install SoX Play from MacPorts or Brew or SourceForge    
------------------------------------------------------------------    
https://superuser.com/questions/279675/installing-sox-sound-exchange-via-the-terminal-in-mac-os-x    
    
https://ports.macports.org/port/sox/    
https://formulae.brew.sh/formula/sox#default    
    
https://sourceforge.net/projects/sox/files/sox/14.3.2/    
https://sourceforge.net/projects/sox/files/sox/14.3.2/sox-14.3.2-macosx.zip/download    
    
    
OPEN bash in that folder    
    
TYPE THIS to install Python3 dependencies:    
------------------------------------------    
  ```sh    
  pip3 install pyautogui    
  pip3 install python_imagesearch    
  ```    
    
TYPE THIS to run the program    
----------------------------    
    
  ```sh    
  python Linux.py    
  ```    
    
to use the Linux Python script from bash
    
    
    
    
    
    
Chromebook Crostini Debian Linux instructions    
=============================================    
  To install Python 3 and SoX on a Chromebook, you will need to use Linux (Crostini), which is the Linux environment available on most recent Chromebooks. Here is how you can set it up:    
    
  Step 1: Enable Linux (Crostini) on your Chromebook    
  --------------------------------------------------    
  
  Open Settings on your Chromebook.    
    
  Scroll down and find Linux (Beta) under the "Developers" section.    
    
  Click Turn On and follow the instructions to set up Linux.    
  This will take a few minutes.    
    
  Step 2: Update Debian Linux packages    
  ------------------------------------    
  
  Once Linux is installed, you will need to open the Linux Terminal.    
  You can find this by searching for "Terminal" in your app launcher.    
    
  Open the terminal and run the following command to update your Linux environment:    
    
    
  ```sh    
  sudo apt update && sudo apt upgrade    
  ```    
    
  Step 3: Install Python 3    
  ------------------------    
  
  To install Python 3, run the following command:    
    
    
  ```sh    
  sudo apt install python3    
  ```    
    
  Once installed, you can check the Python version by typing:    
    
    
  ```sh    
  python3 --version
  ```    
    
  Step 4: Install SoX Play (Sound eXchange)    
  -----------------------------------------    
  
  To install SoX, run the following command:    
    
    
  ```sh    
  sudo apt install sox    
  ```    
    
  To check if SoX was installed successfully, type:    
    
  ```sh    
  sox --version    
  ```    
  
  Optional: If you need MP3 support for SoX, you can install the required libraries with:    
    
    
  ```sh    
  sudo apt install sox libsox-fmt-mp3    
  ```    
    
  Step 5: Test SoX Play    
  ---------------------    
  
  To verify that SoX is working, you can try running a basic command. For example, play a test tone with the following command:    
    
  ```sh    
  play -n synth 3 sine 440    
  ```    
    
  This should play a 3-second sine wave at 440 Hz.    
    
  Once these steps are complete, you will have both Python 3 and SoX installed and ready to use on your Chromebook!    
    
    
  Step 6: Install cURL, wget and unzip    
  ------------------------------------    
    
  ```sh    
    sudo apt install curl wget unzip    
    curl --version    
    wget --version    
    unzip -v    
  ```    
    
    
  Step 7: Install Python3 and X11 extensions    
  ------------------------------------------    
  ```sh    
  sudo apt install python3-pip python3-tk python3-dev python3-pip python3-setuptools python3-wheel libx11-dev libjpeg-dev libpng-dev zlib1g-dev libglib2.0-0    
  sudo apt install x11-utils libx11-dev libxext-dev xauth    
  sudo apt install x11-apps  libx11-dev libxext-dev libxrandr-dev    
  ```    
    
    
  Step 8: Install Python3 AI libraries    
  ------------------------------------    
  ```sh    
  sudo pip3 install --break-system-packages pyautogui    
  sudo pip3 install --break-system-packages python_imagesearch    
  ```    
    
    
  Step 9: Install XAuth for ROOT user    
  -----------------------------------    
  ```sh    
  sudo apt install xauth
  sudo cp ~/.Xauthority /root/.Xauthority 
  echo $DISPLAY
  export DISPLAY=:0
  ```    
    
    
  Step 10: Download, extract this Python3 script under your home directory    
  ------------------------------------------------------------------------    
  ```sh    
  cd ~    
  curl -j -k --output beep.zip https://codeload.github.com/fdd26/Exchange-Beep/zip/refs/heads/main?filename=beep.zip    
  unzip ./beep.zip    
  cd ./Exchange-Beep-main/    
  ls -lFa Linux.py    
  ```    
    
  Step 11: Run this Python3 script under your home directory    
  ----------------------------------------------------------    
  ```sh    
  cd ~/Exchange-Beep-main/    
  python3 Linux.py    
  ```    
    
    
Original Python3 script forked from:    
====================================    
  https://github.com/TotalBattleBots/Exchange-Beep    
    
    
A showcase of what this does can be found at :    
A guide to install this can be found at      :    
    