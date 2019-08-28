########## CHAPTER 8 ############


import os   # https://docs.python.org/3.4/library/os.path.html

os.path.join('usr', 'bin', 'spam') # add folder and file separator
                        # depending on which Operating System is used by user



myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(os.path.join('C:\\users\\arts', filename))

"""
    Any filenames or paths that do not begins with the root folder are assumed
    to be under the current working dictionary.
                                                    """

os.getcwd() # current working directory
'os.chdir(\'C:\\ path\')' # change current working directory


# Absolute vs Relative path
## .\  - current folder
## ..\ - parental folder

# files management
## os.makedirs('C:\\delicious\\walnut\\waffles')  - creates folder/or all path

'os.path.abspath(path)'   # returns a string of the absolute path of the argument
'os.path.isabs(path)' # returns True if the argument is an absolute path
'os.path.relpath(path, start)'    # returns a string of a relative path
                                    # from the start path to path

os.path.abspath('.')    # returns absolute path to current directory
os.path.relpath('C:\\Windows', 'C:\\')
os.path.relpath('C:\\Windows', 'C:\\spam\\eggs')
os.getcwd()
'os.chdir(path)'  # changes current working directory on the 'path'

filePath = 'C:\\Windows\\System32\\calc.exe'
os.path.basename(filePath)  # returns 'calc.exe'
os.path.dirname(filePath)   # returns 'C:\\Windows\\System32'

os.path.split(filePath)     # returns tuple w/ both base and dirname

filePath.split(os.path.sep)

# Files size and Folders content
## os.path.getsize(path)    - returns size in bytes of the file in the path
## os.listdir(path)         - returns a list of filename strings in the path

os.path.getsize('C:\\Windows\\System32\\calc.exe')
os.listdir('C:\\Windows\\System32')

totalSize = 0
for filename in os.listdir('C:\\Windows\\System32'):
    totalSize += os.path.getsize(os.path.join('C:\\Windows\\System32', filename))

print(totalSize)

totalSize2 = 0
for filename in os.listdir('.'):
    totalSize2 += os.path.getsize(os.path.join('.', filename))

print(totalSize2)

# check whether a given path exists and whether it is a file or folder
os.path.exists(path)    # True if file/folder exists
os.path.isfile(path)    # True if file
os.path.isdir(path)     # True if folder
