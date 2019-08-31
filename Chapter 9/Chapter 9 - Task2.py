#! python3
# The program finds the files (from certain location - including subfolders)
# with size over 100MB and print absolute path on the screen.

import os

def list_bigFiles(path):
    path = os.path.abspath(path)
    for foldername, subfolders, filenames in os.walk(path):
        # the size of the folder is NOT size of his files - folder is treated like set of information.
        for subfolder in subfolders:
            print('Size of folder: ' + subfolder + ' is :  ' + str(os.path.getsize(os.path.join(foldername, subfolder))) + ' bytes')
        for filename in filenames:
            if os.path.getsize(os.path.join(foldername, filename)) >= 1048576:
                print(os.path.abspath(filename) + ' :  ' + str(os.path.getsize(os.path.join(foldername, filename)) / (1024*1024)) + ' MB')

list_bigFiles('X:\\path\\somewhere')
