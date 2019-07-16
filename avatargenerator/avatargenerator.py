from PIL import ImageFont, ImageDraw, Image
import sys
from random import randint, random
import colorsys


IMAGE_SIZE = 512
BKG_COLORS = ["#5d3578", "#76347a", "#b04285", "#db497d", "#e76e50","#60487b","#4c7fa2","#4ca29b","#5baf76","#8fb76b","#b4b76b","#b7946b","#b7706b"]
FONT_STYLE = "fonts/UbuntuMono-Bold.ttf"
FONT_COLOR = '#ffffff'
SHADOW = True
SHADOW_STEP = 1     # can be increased to speed up shadow generation (but lowers quality)


def hex_to_rgb(h):
    ''' takes hex in format: #ffffff ; returns tuple of three (r,g,b) '''
    return tuple([int(i,16)/256 for i in [h[1:3], h[3:5], h[5:7]]])


def rgb_to_hex(rgb):
    ''' takes tuple (r,g,b), returns in hex format #ffffff '''
    return "#{:02x}{:02x}{:02x}".format(int(rgb[0]*256),int(rgb[1]*256),int(rgb[2]*256))
    
    
def getRandomColor():
    h = random()
    s = 0.41
    v = 0.61
    return rgb_to_hex(colorsys.hsv_to_rgb(h,s,v))


def makeColorHexDarker(color_hex):
    r,g,b = hex_to_rgb(color_hex)
    h,s,v = colorsys.rgb_to_hsv(r,g,b)
    h,s,v = makeHSVDarker(h,s,v)
    return rgb_to_hex(colorsys.hsv_to_rgb(h,s,v))


def makeHSVDarker(h,s,v):   
    return h,s,max(v-0.2, 0)    # making it darker, but making sure not to get negative number


def generateLetterAvatar(letter1, letter2='', size=IMAGE_SIZE, dir_path='', file_name=''):
    text = letter1[0].upper()
    if letter2:
        text += letter2[0].upper()
    bkg_color=getRandomColor()
    if letter2:         # two letter avatar
        font_size = int(IMAGE_SIZE/1.28)
        text_x = int(IMAGE_SIZE/10)
        text_y =int(IMAGE_SIZE/12.8)
    else:         # one letter avatar
        font_size = int(IMAGE_SIZE*1.2)
        text_x = int(IMAGE_SIZE/5)
        text_y = int(-IMAGE_SIZE/8)
          
    image = Image.new('RGBA', (IMAGE_SIZE,IMAGE_SIZE), bkg_color)
    d = ImageDraw.Draw(image)
    font = ImageFont.truetype(FONT_STYLE, font_size)
    if SHADOW:
        shadow_length = int(IMAGE_SIZE/1.6) 
        for i in range(1,int(shadow_length/SHADOW_STEP)):
            d.text((text_x+i*SHADOW_STEP,text_y+i*SHADOW_STEP), text, font=font, fill=makeColorHexDarker(bkg_color))
    d.text((text_x,text_y), text, font=font, fill=FONT_COLOR)
    
    if size != IMAGE_SIZE:
        image = image.resize((size, size), Image.LANCZOS)  
        # LANCZOS supposed to be the best resizing method
    
    if not file_name:  
        file_name = str(int(random()*10000000)) + '.png'
    image.save(dir_path+file_name, "")
    
    return dir_path+file_name


if __name__ == "__main__":
    
    if(len(sys.argv)>2):
        generateLetterAvatar(sys.argv[1][0], sys.argv[2][0])
    else:
        generateLetterAvatar(sys.argv[1][0])      # first letter of 
    