#! python3
#  -    Identyfing Photo Folders on the HardDrive.
#           Photo Folder is a folder which consists in 50% or more of 'png'
#           or 'jpeg' photo with size of width and heigh larger than 500.
#           As a result the absolute path of "Photo Folder" will be printed.

import os
from PIL import Image

for folderName, subfolders, filenames in os.walk('F:\\'):
    numPhoto = 0
    numFiles = 0
    folder = os.path.abspath(folderName)
    for filename in filenames:
        numFiles += 1
        if not (filename.lower().endswith('.png') or \
                filename.lower().endswith('.jpeg') or \
                filename.lower().endswith('.jpg')):
            continue
        im = Image.open(os.path.join(folder, filename))
        width, height = im.size
        if width>900 and height>900:
            numPhoto += 1
    if numPhoto * 2 >= numFiles and numFiles != 0:
        print(folder)
                                           
