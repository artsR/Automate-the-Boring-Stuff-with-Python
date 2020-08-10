######### CHAPTER 18 ##########

import pyautogui, time

# 'PyAutoGUI' has screenshot features that can create an image file based on
# the current contents of the screen. (It can also create Pillow Image Object).

im = pyautogui.screenshot() # makes a screenshot. Returns Image Object.
print(im.getpixel((0,0)))
print(im.getpixel((50,200)))

print(pyautogui.pixelMatchesColor(50,200, (255,255,255))) #checks if the pixel
#               of given coordinates matches to color passed in third argument.
'''
print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        pixelColor = pyautogui.screenshot().getpixel((x,y))
        positionStr += ' RGB: (' + str(pixelColor[0]).rjust(3)
        positionStr += ', ' + str(pixelColor[1]).rjust(3)
        positionStr += ', ' + str(pixelColor[2]).rjust(3) + ')'
        print(positionStr)
except KeyboardInterrupt:
    print('You quit program.')
'''
# Image Recognition:
area = pyautogui.locateOnScreen('area.png') # returns 4 coordinates.
print(area)
list(pyautogui.locateAllOnScreen('area.png'))
pyautogui.click(pyautogui.center(area)) # returns center of given area.
