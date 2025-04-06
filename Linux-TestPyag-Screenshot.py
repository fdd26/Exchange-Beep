#!python3

import os
import time
import mss

import pyautogui

screenshot = pyautogui.screenshot()
screenshot.save("screenshot-pyag.png")
