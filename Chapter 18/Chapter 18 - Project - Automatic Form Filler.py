#! python3
# formFiller.py - Automatic Form Filler.


import pyautogui, time

pyautogui.PAUSE = 0.5

nameField = (854, 417)
submitButton = (766, 554)
submitButtonColor = (66, 133, 244)
submitAnotherLink = (879, 337)

formData = [{'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand',
             'robocop': 4, 'comments': 'Tell Bob I said hi.'},
            {'name': 'Bob', 'fear': 'bees', 'source': 'amulet',
             'robocop': 4, 'comments': 'n/a'}, 
            {'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball',
             'robocop': 1, 'comments': 'Please take the puppets out of the break room.'},
            {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money',
             'robocop': 5, 'comments': 'Protect the innocent. Serve the public trust. Uphold the law.'},
            ]

for person in formData:
    print('>>>> 2 SECONDs PAUSE to LET YOU PRESS Ctrl-C to stop <<<<')
    time.sleep(2)

    # Wait until the form page has loaded:
##    while not pyautogui.pixelMatchesColor(submitButton[0], submitButton[1],
##                                     submitButtonColor):
    time.sleep(0.5)
    print('Entering %s info...' % (person['name']))
    pyautogui.click(nameField)

    # Fill out the Name field:
    pyautogui.typewrite(person['name'] + '\t')

    # Fill out the Greatest Fear field:
    pyautogui.typewrite(person['fear'] + '\t')

    # Fill out the Source of Wizard Power field:
    if person['source'] == 'wand':
        pyautogui.typewrite(['down', 'enter'])
        pyautogui.press('tab')
    elif person['source'] == 'amulet':
        pyautogui.typewrite(['down', 'down', 'enter'])
        pyautogui.press('tab')
    elif person['source'] == 'crystal ball':
        pyautogui.typewrite(['down', 'down', 'down', 'enter'])
        pyautogui.press('tab')
    elif person['source'] == 'money':
        pyautogui.typewrite(['down', 'down', 'down', 'down', 'enter'])
        pyautogui.press('tab')

    # Fill out the RoboCop field:
    if person['robocop'] == 1:
        pyautogui.typewrite([' ', '\t'])
    elif person['robocop'] == 2:
        pyautogui.typewrite(['right', '\t'])
    elif person['robocop'] == 3:
        pyautogui.typewrite(['right', 'right', '\t'])
    elif person['robocop'] == 4:
        pyautogui.typewrite(['right', 'right', 'right', '\t'])
    elif person['robocop'] == 5:
        pyautogui.typewrite(['right', 'right', 'right', 'right', '\t'])

    # Fill out the Additional Comments field:
    pyautogui.typewrite(person['comments'] + '\t')
    time.sleep(1)
    
    # Click Submit:
    pyautogui.press('enter')

    #Wait until form page has loaded:
    print('Form submitted.')
    time.sleep(5)

    # Click the link to another form:
    pyautogui.click(submitAnotherLink)
