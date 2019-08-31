########## CHAPTER 9 ############

# shutil Modul (shell utilities) has functions to let me copy, move, rename
#       and delete files in my Python programs.

import shutil, os
import send2trash # safe deletes files and folders - it sends file to trash
import zipfile

# shutil.copy(source, destination) - copies file at the path source to the
    # folder at the path destination.
    # if the destination is a file, it will be used as the new name of the
        # copied file.
    # returns a string of the path of the copied file.
# shutil.copytree() - copies an entire folder and every folder and file
    # contained in it.

# shutil.move(source, destination) - moves the file/ folder at the path source
    # to the path destination.
    # returns absolute path to the new location
    # if destination is a file the file will be renamed.
    # if destination folder doesn't exist, then the name of file will be
        # changed and destination will be treated as a new name for a file.
    
# os.unlink(path)   - deletes the file at path
# os.rmdir(path)    - deletes the folder at path
# shutil.rmtree(path)-removes the folder at path, and all files/folders in it.


'''
    Mistake in deleting wrong files may cost a lot, therefore
    it is recommendable to put calls in comment and first of all
    printed all names of file which I'm going to delete:
                                                                    '''
for filename in os.listdir():
    if filename.endswith('.txt'):
        ##os.unlink(filename)
        print(filename)

baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon in not a vegetable.')
baconFile.close()
# send2trash.send2trash('bacon.txt')


# Changing names of files in certain folder and his subfolders
for folderName, subfolders, filenames in os.walk('C:\\delicious'):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': ' + filename)

    print('')
    # os.walk(folder) - returns 3 values on each iteration through the loop:
        # a string of the current folder's name
        # a list of strings of the folders in the current* folder
        # a list of strings of the files in the current* folder
        # * curent folder for the current iteration


# zipfile Module
## reading zip Files
# exampleZip = zipfile.ZipFile('example.zip') 
# exampleZip.namelist() # list of strings with names of files/folders
# spamInfo = exampleZip.getinfo('spam.txt')
# spamInfo.file_size
# spamInfo.compress_size
# print('Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo.compress_size, 2))
# exampleZip.close()

## extracting zip Files
# exampleZip = zipfileZipFile('example.zip')
# exampleZip.extractall()   # extracts all files/folders into a current work.dict.
    # exampleZip.extractall(path) # extract all into a path (create if doesn't exist)
    # exampleZip.extract(file, path)  # extract only file into a path
                # returns absolute path to which the file was extracted.
# exampleZip.close()

## creating and adding zip Files
# newZip = zipfile.ZipFile('new.zip', 'w') # overwriting existing
# newZip = zipfile.ZipFile('existing.zip', 'a') # possibility to add files w/o overwriting
# newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
# newZip.close()

