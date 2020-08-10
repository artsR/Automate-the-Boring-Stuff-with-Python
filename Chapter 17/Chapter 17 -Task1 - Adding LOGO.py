#! python3
# AddLogo.py -  Resizes all images in current working directory to fit in a
#               300x300 square, and adds catlogo.png to the lower-right corner.

import os
from PIL import Image, ImageColor

SQUARE_FIT_SIZE = 300           # this is the way I define CONSTANT_VARIABLE
LOGO_FILENAME = 'catlogo.png'   # CONSTANT_VARIABLE

logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size

os.makedirs('Chapter 17', exist_ok=True)
folder = os.path.abspath('Chapter 17')

for filename in os.listdir('.'):
    if not (filename.lower().endswith('.png') or filename.lower().endswith('.jpg') \
       or filename.lower().endswith('.gif') or filename.lower().endswith('.bmp')) \
       or filename == LOGO_FILENAME:
        continue    # skip non-image files and skip logo file.
    im = Image.open(filename)
    width, height = im.size

    if width < logoWidth or height < logoHeight:
        print('Adding logo to %s was skipped.' % (filename))
        continue
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        # Calculate the new width and height to resize to:
        if width > height: # I don't have to check it. I can do it versatilely.
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE

        # Resize the image:
        print('Resizing %s...' % (filename))
        im.resize((width, height)) # changes are made in this place.
        #                            The new Image Object is NOT returned.
    # Add the logo:
    print('Adding logo to %s...' % (filename))
    im.paste(logoIm, (width-logoWidth, height-logoHeight), logoIm)

    # Save new file with logo:
    im.save(os.path.join(folder, os.path.splitext(filename)[0]+'_withLogo'+
                         os.path.splitext(filename)[1]))
    
# Ideas for similar programs:
## Add text or a website URL to images.
## Add timestamp to images.
## Copy or move images into different folders based on their sizes.
## Add a mostly transparent watermark to an image to prevent other from copying it.

