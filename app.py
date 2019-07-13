from PIL import ImageFont, ImageDraw, Image
import sys
from random import randint

#import argparse

IMAGE_SIZE = 1024
BKG_COLORS = ["#5d3578", "#76347a", "#b04285", "#db497d", "#e76e50","#60487b","#4c7fa2","#4ca29b","#5baf76","#8fb76b","#b4b76b","#b7946b","#b7706b"]
FONT_COLOR = '#ffffff'
FONT_STYLE = "fonts/UbuntuMono-Bold.ttf"

def getRandomColor():
    return BKG_COLORS[randint(0,len(BKG_COLORS)-1)]

def generateLetterAvatar(letter1, letter2='', shadow=True):
    font_size = 1228 
    text_x = 203
    text_y = -128
    text = letter1.upper()+letter2.upper()
    if letter2:
        font_size = 800 
        text_x = 103
        text_y = 90
    image = Image.new('RGBA', (IMAGE_SIZE,IMAGE_SIZE), getRandomColor())
    d = ImageDraw.Draw(image)
    font = ImageFont.truetype(FONT_STYLE, font_size)
    font2 = ImageFont.truetype(FONT_STYLE, font_size)
    if shadow:
        for i in range(1,700):
            d.text((text_x+i,text_y+i), text, font=font2, fill="#444444")
    d.text((text_x,text_y), text, font=font, fill=FONT_COLOR)
    image.show()
    

if __name__ == "__main__":
        
    if(len(sys.argv)>2):
        generateLetterAvatar(sys.argv[1][0], sys.argv[2][0])
    else:
        generateLetterAvatar(sys.argv[1][0])      # first letter of 
    
#    print(sys.argv[1])
#    print(sys.argv[2])
#    print(sys.argv[3])
    
#    parser = argparse.ArgumentParser()
#    parser.add_argument(
#        '--l1',
#        help='first letter of the avatar',
#        default ='A',
#        required=True
#    )
#    parser.add_argument(
#        '--l2',
#        help='second letter of the avatar',
#        default =''
#    )
#    args = parser.parse_args()
#    
#    
#    if not args.l2:
#        genOneLetterAvatar(args.l1)
#    else:
#        genTwoLettersAvatar(args.l1, args.l2)
        
    
