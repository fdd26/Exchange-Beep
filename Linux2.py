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
#import pyautogui as pag
import time
from python_imagesearch.imagesearch import imagesearch

# Merc frequency is set to 500Hz
freqMerc = 500

# Gold frequency is set to 800Hz
freqGold = 800

# duration is set to 100 milliseconds
dur = 0.500


# Forever loop...
while True:
    # 100% resolution square image search
    pos = imagesearch("exchange1.png")
    if pos[0] != -1:
        winsound.Beep(freqMerc, dur)
        del pos

    # 25% resolution square image search with truncation
    pos = imagesearch("exchange2.png")
    if pos[0] != -1:
        os.system('play -n synth {} sine {}'.format(dur, freqMerc))  # Play if find "exchange"
        del pos

    # Truncation search works with side arrows
    pos = imagesearch("exchange3.png")
    if pos[0] != -1:
        os.system('play -n synth {} sine {}'.format(dur, freqMerc))  # Play if find "exchange"
        del pos

    # Truncation search works with bottom arrows
    pos = imagesearch("exchange4.png")
    if pos[0] != -1:
        os.system('play -n synth {} sine {}'.format(dur, freqMerc))  # Play if find "exchange"
        del pos

    # Truncation search works with bottom arrows
    pos = imagesearch("gold-dm1.png")
    if pos[0] != -1:
        os.system('play -n synth {} sine {}'.format(dur, freqGold))  # Play if find "gold-dm"
        del pos

    # Truncation search works with bottom arrows
    pos = imagesearch("gold-dm2.png")
    if pos[0] != -1:
        os.system('play -n synth {} sine {}'.format(dur, freqGold))  # Play if find "gold-dm"
        del pos

    # Sleep a little before looping
    time.sleep(0.05)
