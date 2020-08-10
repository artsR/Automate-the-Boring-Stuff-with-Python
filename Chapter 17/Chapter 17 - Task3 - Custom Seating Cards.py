#! python3
#  -    Creates images for Custom Seating Cards for my guests
#       (listed in 'guests.txt'). Every card has the same size 4x5 inch.
#       (Pillow produces image with 72 pixels per inch: 900x460 pixels)


from PIL import Image, ImageDraw, ImageFont
    
guestFile = open('guests.txt')
guests = guestFile.readlines()
guestFile.close()

for guest in guests:
    flowerIm = Image.open('SeatCard_Crown.png') # Transparent image for Seat Card.
    seat_cardIm = Image.new('RGBA', (254, 146), 'white')
    #seat_cardIm.paste(flowerIm, (190,25), flowerIm)

    name = guest.strip('\n')
    drawObj = ImageDraw.Draw(seat_cardIm)
    drawObj.line([(0,0), (253,0), (253,145), (0,145), (0,0)], fill='black')
    myFont = ImageFont.truetype('arial.ttf', 20)
    sizeText = drawObj.textsize(name, font=myFont)
    drawObj.text((int((254-sizeText[0])/2),int((146-sizeText[1])/2)),
                 name, fill='black', font=myFont)
    seat_cardIm.paste(flowerIm, (254-int((254-sizeText[0])/2)-20,25), flowerIm)
    seat_cardIm.save('SeatCard_'+name+'.png')
