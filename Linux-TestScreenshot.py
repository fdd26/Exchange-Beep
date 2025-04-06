#!python3

import os
import time
import mss

with mss.mss() as sct:
    # Print all available monitors
    print(sct.monitors)

    # Try grabbing a specific monitor (e.g., the first one)
    screenshot = sct.grab(sct.monitors[1])  # Adjust index if needed
    screenshot.save("screenshot1.png")
    
    # Try grabbing a specific monitor (e.g., the first one)
    screenshot = sct.grab(sct.monitors[2])  # Adjust index if needed
    screenshot.save("screenshot2.png")
    
    # Try grabbing a specific monitor (e.g., the first one)
    screenshot = sct.grab(sct.monitors[0])  # Adjust index if needed
    screenshot.save("screenshot0.png")
