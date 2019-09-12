#! python3
# mapIt.py - takes an address from command line as argument and open
# Google Maps showing this place on the map.
# If there is no command line argument, then program will use the content
# of the clipboard

import webbrowser, pyperclip, sys

if len(sys.argv[1]) > 1:
    #Get address from command line
    address = ' '.join(sys.argv[1:]) # sys.argv is a list of strings
else:
    address = pyperclip.paste()

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
webbrowser.get(chrome_path).open('https://www.google.com/maps/place/' + address)

# what else I can do:
## open all links on a page in separate browser tabs
## open the browser to the URL for my local weather
## open several social network sites that I regularly check
