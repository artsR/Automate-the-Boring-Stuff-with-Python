######### CHAPTER 18 ############


import pyautogui

##pyautogui.click(10, 700)
##pyautogui.typewrite('Hello World!',0.25) # sends virtual keypresses to computer.
##pyautogui.typewrite(['enter','a','b','left','left','X','Y','enter'], 0.25)

#print(pyautogui.KEYBOARD_KEYS) # returns list all possible KEY strings.

pyautogui.keyDown('shift')
pyautogui.press('4')
pyautogui.keyUp('shift')

#------------------------
pyautogui.keyDown('ctrl')
pyautogui.keyDown('c')
pyautogui.keyUp('c')
pyautogui.keyUp('ctrl')
# the same I can achieve useing '.hotkey()':
pyautogui.hotkey('ctrl', 'c') # takes multiple keyboard key string argument,
#                   presses them in order, and releases them in reverse order.

def commentAfterDelay():
    pyautogui.click(10,700)
    pyautogui.typewrite('In IDLE, Alt-3 comments out a line.')
    time.sleep(2)
pyautogui.hotkey('alt','3')

commentAfterDelay()
