########## CHAPTER 17 ###########


from PIL import ImageColor, Image

# In 'pillow' Module, RGBA values are represented by a tuple of 4 integers:
#   "Red, Green, Blue, transparency" - = transparency: 0 = invisible.

# https://en.wikipedia.org/wiki/Web_colors
print(ImageColor.getcolor('red', 'RGBA')) # returns tuple with RGBA
print(ImageColor.getcolor('RED', 'RGBA'))
print(ImageColor.getcolor('black', 'RGBA'))
print(ImageColor.getcolor('chocolate', 'RGBA'))
print(ImageColor.getcolor('CornFlowerBlue', 'RGBA'))

# Coordinates of Image:
#   They represent location of pixels on the picture.
## (0,0) top-left: 'origin' - (x,y)
#       x - left --> right
#       y - top  --> down
## 'box tuple' : (rectangule) left(x) -> top(y) -> right(x) -> bottom(y)


# Working with the Image Data Type:
catIm = Image.open('zophie.png')
print(catIm.size)
width, height = catIm.size
print(str(width) +' and ' + str(height))
print(catIm.filename)
print(catIm.format)
print(catIm.format_description)
catIm.save('zophie.jpg') # I can convert the image from PNG to JPG format.

# Create new Image:
## 'RGBA' - set the color mode.
## (x, y) - set width and height of image.
## (R, G, B, A) or 'colorName' - initial background color for image.
newImage = Image.new('RGBA', (100,200), 'purple')
newImage.save('purpleImage.png')
newerImage = Image.new('RGBA', (20,20))
newerImage.save('transparentImage.png')

# Cropping Image:
croppedImage = catIm.crop((335,345,565,560)) # takes as an argument 'tuple'
croppedImage.save('croppedImage.png')

# Copying and Pasting Image into other Image:
catIm_copy = catIm.copy()
catIm_copy.paste(croppedImage, (0, 0))
catIm_copy.paste(croppedImage, (570, 500))# (x, y) coordinates where croppedImage
#                                   will be pasted.
catIm_copy.save('pastedImages.png')

faceImageWidth, faceImageHeight = croppedImage.size
pilesImage = Image.new('RGBA', (1380, 1290))
pilesWidth, pilesHeight = pilesImage.size

for left in range(0, pilesWidth, faceImageWidth):
    for top in range(0, pilesHeight, faceImageHeight):
        print(left, top)
        pilesImage.paste(croppedImage, (left, top))
pilesImage.save('pilesImage.png')

## 'Mask' object:
#   pilesImage.paste(croppedImage, (left, top), 'Image_Object')
#       'Image_Object' contains transparent pixels. This 3rd argument take into
#       account only 'transparency' value from 'RGBA'. The Red,Green,Blue are
#       ignored.

# Resizing Image:
quartersizedCat = catIm.resize( (int(width/2), int(height/2)) ) #returns new image
quartersizedCat.save('zophieSMALL.png')

# Rotating and Flipping Image:
catIm.rotate(90).save('zophie90.png')   # returns new Image. 'catIm' is unchanged
catIm.rotate(90, expand=True).save('zophie90_expanded.png') # the area of image
#                                           is expanded - Image isn't cut.
catIm.rotate(270).save('zophie270.png') # like above.
catIm.rotate(6).save('zophie6.png')
catIm.rotate(6, expand=True).save('zophie6_expanded.png')#doesn't cut the image.
#                                       All part of image is visible.
catIm.transpose(Image.FLIP_LEFT_RIGHT).save('zophie_flip_horizontal.png')
catIm.transpose(Image.FLIP_TOP_BOTTOM).save('zophie_flip_vertical.png')

# Changing individual Pixels:
managePixels = Image.new('RGBA', (100, 100))
print(managePixels.getpixel( (0, 0) ))
for x in range(100):
    for y in range(50):
        managePixels.putpixel( (x,y), (210,210,210) )

for x in range(100):
    for y in range(50, 100):
        managePixels.putpixel( (x,y), ImageColor.getcolor('darkgray', 'RGBA'))
print(managePixels.getpixel( (0,0) ))
print(managePixels.getpixel( (0,50) ))
managePixels.save('managePixels.png')

# Drawing on Image:
from PIL import ImageDraw, ImageFont
#        http://pillow.readthedocs.org/en/latest/reference/ImageDraw.html

im = Image.new('RGBA', (200,200), 'white')
drawObj = ImageDraw.Draw(im) #this new object has several useful method.
## 'point(xy, fill)' draws individual pixels.
#       xy - list of the points I want to draw
        #   [ (x,y), (x,y), ...] or
        #   [x1, y1, x2, y2, ..
#       fill - color of the points (RGBA tuple or string of color name)(optional)

## 'line(xy, fill, width)' draws line.
#       width - width of the line

## 'rectangle(xy, fill, outline)' draws a rectangle.
#       xy - (left, top, right, bottom)
#       outline - color of rectangle's outline

## 'ellipse(xy, fill, outline)' draws an ellipse.
## 'polygon(xy, fill, outline)' draws an arbitrary polygon.
#       xy - list of the points I want to draw
        #   [ (x,y), (x,y), ...] or
        #   [x1, y1, x2, y2, ...]

drawObj.line([(0,0), (199,0), (199,199), (0,199), (0,0)], fill='black')
drawObj.rectangle((20,30,60,60), fill='blue')
drawObj.ellipse((120,30,160,60), fill='red')
drawObj.polygon(((57,87),(79,62),(94,85),(120,90),(103,113)), fill='brown')

for i in range(100, 200, 10):
    drawObj.line([(i,0),(200, i-100)], fill='green')
# all modifications made on drawObj are reflected on 'im' variable, so
# I need to save 'im' variable, NOT 'drawObj' variable:
im.save('drawing.png')

## 'text(xy, text, fill, font)' draws text onto image.
#       xy - (x, y) specifies the upper-left corner of the text box
#       font - 'ImageFont' Object used to set the typeface and size of text:
arialFont = ImageFont.truetype('arial.ttf', 32)#font, size
drawObj.text((20,150), 'Hello', fill='pink')
drawObj.text((100,150), 'Howdy', fill='gray', font=arialFont)
im.save('drawing_text.png')

### textsize(text, font): returns tuple of width and height of text.
