########## CHAPTER 18 ###########


import pyautogui, time
# http://pyautogui.readthedocs.org/

pyautogui.PAUSE = 1.5 # stops doing programs for 1.5 second
pyautogui.FAILSAFE = True# crashes program if mouse will be in upper-left corner


# Control Mouse Movement:
'''   SCREEN (1920x1080 resolution)

(0,0)                      (1919,0)





(0,1079)                (1919,1079)
                                        '''
'''
pyautogui.size() # returns tuple with width and height of the screen [pixels]
width, height = pyautogui.size()

for i in range(2):
    pyautogui.moveTo(100,100, duration=0.25) # duration of movement 0.25 sec.
    pyautogui.moveTo(200,100, duration=0.25)
    pyautogui.moveTo(200,200, duration=0.25)
    pyautogui.moveTo(100,200, duration=0.25)
    
for i in range(2):
    pyautogui.moveRel(100,0, duration=0.25) # coordinates are relative.
    pyautogui.moveRel(0,100, duration=0.25)
    pyautogui.moveRel(-100,0, duration=0.25)
    pyautogui.moveRel(0,-100, duration=0.25)

pyautogui.position() # returns actual mouse position.
'''

#******************************************************
#************WHERE IS THE MOUSE RIGHT NOW ? ***********
#******************************************************
''''''
print('Press Ctrl-C to quit.')
positionStr = []
filePos = open('position.txt', 'w')
try:
    while True:
        x, y = pyautogui.position()
        positionStr.append(str(x)+','+str(y))
        print(x,y)
        time.sleep(2)
except KeyboardInterrupt:
    filePos.write('\n'.join(positionStr))
    filePos.close()
    print('You quit program.')
'''

# Clicking the Mouse:

pyautogui.click(800,250, button='right')  # right click at specified coordinates
pyautogui.click(100,150, button='left')   # left click at specified coordinates

pyautogui.mouseDown()   # press mouse button
pyautogui.mouseUp()     # release mouse button

pyautogui.doubleClick() # double click of left button
pyautogui.rightClick()  # right button click
pyautogui.middleClick() # middle button click

# Dragging the Cursor - move it with pressed one button:

time.sleep(5)
pyautogui.click()
distance = 200
while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0.2)
    distance -= 5
    pyautogui.dragRel(0, distance, duration=0.2)
    distance -= 5
    pyautogui.dragRel(-distance, 0, duration=0.2)
    distance -= 5
    pyautogui.dragRel(0, -distance, duration=0.2)

# Scrolling the Mouse:
pyautogui.click(800,300, button='left')
pyautogui.scroll(-500)
'''
