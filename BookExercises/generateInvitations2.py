#! python3
# generateInvitations.py

import os
from PIL import Image, ImageDraw, ImageFont

imFlowers = Image.open('Flowers.png')
imFlowers = imFlowers.resize((268,340))
guestFile = open('guests.txt')
guests = guestFile.readlines()
guestFile.close()
os.makedirs('invitations', exist_ok=True)
for guest in guests:
    im = Image.new('RGBA', (288,360), 'white')
    im.paste(imFlowers,(10,10))
    fontsFolder = '/usr/share/fonts/truetype'
    carlitoItalicFont = ImageFont.truetype(os.path.join(fontsFolder,'Carlito-Italic.ttf'), 12)
    draw = ImageDraw.Draw(im)
    draw.line([(10,10), (278,10), (278,350), (10,350), (10,10)], fill='black')
    draw.text((20,80),'It would be a pleasure to have the company of',fill='purple', font=carlitoItalicFont)
    draw.text((110,110),guest,fill='purple', font=carlitoItalicFont)
    draw.text((130,140),'at',fill='purple', font=carlitoItalicFont)
    draw.text((40,170),'11011 Memory Lane on the Evening of',fill='purple', font=carlitoItalicFont)
    draw.text((110,200),'April 1st',fill='purple', font=carlitoItalicFont)
    draw.text((130,230),'at',fill='purple', font=carlitoItalicFont)
    draw.text((110,260),'7 o\' clock',fill='purple', font=carlitoItalicFont)
    filename = guest.rstrip() + '.png'
    im.save(os.path.join('invitations', filename))

    
