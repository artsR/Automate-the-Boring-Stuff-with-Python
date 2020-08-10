#! python3
# nudgeCoursor.py - Nudges coursor every 10 second.


import pyautogui

pyautogui.PAUSE = 10

i = 1
while True:
    pyautogui.moveRel(50 * (-1)**i, 0, duration=2)
    i += 1
