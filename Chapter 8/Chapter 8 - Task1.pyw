#! python3
# Multiclipboard - Saves and loads pieces of text to the clipboard.
# Usage:    py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#           py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#           py.exe mcb.pyw list - Loads all keywords to clipboard.
#           py.exe mcb.pyw delete - Deletes all keywords from list.
#           py.exe mcb.pyw delete <keyword> deletes keyword from list.

import shelve, pyperclip, sys, time

mcbShelf = shelve.open('multiclipboard_Task1')

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1].lower() == 'delete':
        for item in mcbShelf:
        # del list(mcbShelf.keys())[:] it doesn't work
            del mcbShelf[item]
        # pyperclip.copy(str(list(mcbShelf.keys())))
            pyperclip.copy(str(list(mcbshelf.keys())[i]))
            time.sleep(10)
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
