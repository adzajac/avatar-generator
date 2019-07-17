from PIL import ImageFont, ImageDraw, Image
import sys
from random import random
from avatargenerator import colorfunc, utils
from avatargenerator.styles import AvatarStyle


def generateLetterAvatar(letter1, letter2="", styles=AvatarStyle, size=512, dir_path="", file_name=""):
    
    if letter2:
        text = letter1[0].upper() + letter2[0].upper()
        font_size = int(styles.IMAGE_SIZE/1.4)
        text_x = int(styles.IMAGE_SIZE/7)
        text_y =int(styles.IMAGE_SIZE/8)
    else:         # one letter avatar
        text = letter1[0].upper()
        font_size = int(styles.IMAGE_SIZE*1)
        text_x = int(styles.IMAGE_SIZE/4.0)
        text_y = int(-styles.IMAGE_SIZE/30)
    
    bkg_color=colorfunc.getRandom()
    image = Image.new("RGBA", (styles.IMAGE_SIZE,styles.IMAGE_SIZE), bkg_color)
    draw_image = ImageDraw.Draw(image)
    font = ImageFont.truetype(styles.FONT_STYLE, font_size)
    if styles.SHADOW:
        shadow_length = int(styles.IMAGE_SIZE/1.6) 
        for i in range(1,int(shadow_length/styles.SHADOW_STEP)):
            draw_image.text((text_x+i*styles.SHADOW_STEP,text_y+i*styles.SHADOW_STEP), text, font=font, fill=colorfunc.makeHexDarker(bkg_color))
    draw_image.text((text_x,text_y), text, font=font, fill=styles.FONT_COLOR)
    
    if size != styles.IMAGE_SIZE:
        image = image.resize((size, size), Image.LANCZOS)  
        # LANCZOS supposed to be the best available resizing method
    
    if not file_name:  
        file_name = text+"_" + utils.getRandomString(10) + "_" + str(size) + ".png"
    image.save(dir_path+file_name, "")
    
    return dir_path+file_name


if __name__ == "__main__":
    
    if(len(sys.argv)>2):
        generateLetterAvatar(sys.argv[1][0], sys.argv[2][0])
    else:
        generateLetterAvatar(sys.argv[1][0])      
    