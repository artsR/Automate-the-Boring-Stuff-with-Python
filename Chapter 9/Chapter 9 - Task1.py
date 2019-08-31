#! python 3

"""
    Program walks through a folder tree and seraches for files with
    a certain file extension. Copy these files from whatever location
    they are in to a new folder
                                        """
import shutil, os

def copyMyFile(path, ext):
    path = os.path.abspath(path)
    print(path)
    for foldername, subfolders, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith(ext):
                print(filename + '<--' + foldername)
                if not os.path.exists(os.path.join(path, 'Chapter 9 - Task1', filename)):
                    shutil.copy(filename, os.path.join(path, 'Chapter 9 - Task1'))
            

extension = input('Give me file extension: ')

copyMyFile('.\\', extension)

