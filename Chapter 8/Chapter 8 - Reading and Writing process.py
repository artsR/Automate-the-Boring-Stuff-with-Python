########## CHAPTER 8 ##############

import os, pprint

print(os.getcwd())
helloFile = open(os.path.join(os.getcwd(), 'Chapter 8 - first file.txt'))
        # open('path', 'r/w/a') open file in read mode - returns File Object.

fileContent = helloFile.read() # read entire contents of a file as a string
print(fileContent)
helloFile.close()

helloFile = open(os.path.join(os.getcwd(), 'Chapter 8 - first file.txt'))

fileLine = helloFile.readlines() # list of string (seperated by newline)
print(fileLine)
helloFile.close()

# to change file I should open it in "write" (overwrite) or "append" (add) mode.
    # both 'w' and 'a' mode creates the file if doesn't exist


file = open('Chapter 8 - first file.txt', 'a')
file.write('\n\nEnd of file. Bye!\n')
file.close()

file = open('myCats.py', 'w')
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
pprint.pformat(cats) # it returns string with full format scheme.
file.write('cats = ' + pprint.pformat(cats) + '\n')
file.close()

"""
    Only basic data types such as: integers, floats, strings, lists and
    dictionaries can be written to a file as simple text.
    File objects, for example, cannot be encoded as text.
                                                                """

file = open('Chapter 8 - first file.txt')
print(file.read())
file.close()
