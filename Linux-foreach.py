#!python3

#####################################################################
#
# Works with Python 3.12+
#
# Linux version patch from Polish K103 clan: [PSS] Krzys
#
#
# DOWNLOAD THIS:
# https://codeload.github.com/fdd26/Exchange-Beep/zip/refs/heads/main?file=Exchange-Beep-main.zip
#
# Extract it
#
# OPEN bash in that folder
#
# TYPE THIS to install Python3 dependencies:
# pip3 install pyautogui
# pip3 install python_imagesearch
#
# TYPE THIS to run the program
# python3 Linux.py
#
# OPEN exchange.png to test, you should hear some beeps.
#
#####################################################################
#
# Original Python3 script forked from:
# https://github.com/TotalBattleBots/Exchange-Beep
#
#####################################################################

import os

import time
from python_imagesearch.imagesearch import imagesearch

# Merc frequency is set to 500Hz
freqMerc = 500

# Gold frequency is set to 800Hz
freqGold = 800

# duration is set to 500 milliseconds
dur = 0.500

# List of images
images_to_search = ["exchange1.png", "exchange2.png", "exchange3.png", "exchange4.png", "gold-dm1.png", "gold-dm2.png"]

# Forever loop...
while True:
    for image in images_to_search:
        pos = imagesearch(image)
        if pos[0] != -1:
            if "exchange" in image:
                os.system('play -n synth {} sine {}'.format(dur, freqMerc))  # Play if find "exchange"
            elif "gold-dm" in image:
                os.system('play -n synth {} sine {}'.format(dur, freqGold))  # Play if find "gold-dm"
            del pos
    time.sleep(0.05)