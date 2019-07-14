from PIL import ImageFont, ImageDraw, Image
import sys
from random import randint
import colorsys

#import argparse

MAX_IMAGE_SIZE = 1024
BKG_COLORS = ["#5d3578", "#76347a", "#b04285", "#db497d", "#e76e50","#60487b","#4c7fa2","#4ca29b","#5baf76","#8fb76b","#b4b76b","#b7946b","#b7706b"]
FONT_COLOR = '#ffffff'
FONT_STYLE = "fonts/UbuntuMono-Bold.ttf"

def hex_to_rgb(h):
    ''' h in format: #ffffff ; this function returns tuple of three (r,g,b) '''
    return tuple([int(i,16)/256 for i in [h[1:3], h[3:5], h[5:7]]])

def rgb_to_hex(rgb):
    ''' tuple (r,g,b) to hex in format #ffffff '''
    return "#{:02x}{:02x}{:02x}".format(int(rgb[0]*256),int(rgb[1]*256),int(rgb[2]*256))
    
def getRandomColor():
    return BKG_COLORS[randint(0,len(BKG_COLORS)-1)]

def makeColorDarker(color_hex):
    r,g,b = hex_to_rgb(color_hex)
    h,s,v = colorsys.rgb_to_hsv(r,g,b)
    v = max(v-0.1, 0)       # making it darker, but not to get negative number
    return rgb_to_hex(colorsys.hsv_to_rgb(h,s,v))

def generateLetterAvatar(letter1, letter2='', shadow=True):
    font_size = 1228 
    text_x = 203
    text_y = -128
    text = letter1.upper()+letter2.upper()
    bkg_color=getRandomColor()
    if letter2:
        font_size = 800 
        text_x = 103
        text_y = 90
    image = Image.new('RGBA', (MAX_IMAGE_SIZE,MAX_IMAGE_SIZE), bkg_color)
    d = ImageDraw.Draw(image)
    font = ImageFont.truetype(FONT_STYLE, font_size)
    font2 = ImageFont.truetype(FONT_STYLE, font_size)
    if shadow:
        for i in range(1,700):
            d.text((text_x+i,text_y+i), text, font=font2, fill=makeColorDarker(bkg_color))
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
        
    
