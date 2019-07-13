from PIL import ImageFont, ImageDraw, Image
import sys
from random import randint

#import argparse

IMAGE_SIZE = 1024
color_list = ["#5d3578", "#76347a", "#b04285", "#db497d", "#e76e50"]


def getRandomColor():
    return color_list[randint(0,len(color_list)-1)]

def genOneLetterAvatar(letter):
    font_size = 1228 
    font_color = getRandomColor()
    bkg_color = '#dddddd'
    image = Image.new('RGBA', (IMAGE_SIZE,IMAGE_SIZE), font_color)
    d = ImageDraw.Draw(image)
    font = ImageFont.truetype("fonts/UbuntuMono-Bold.ttf", font_size)
    d.text((203, -128), letter.upper(), font=font, fill=bkg_color)
    image.show()
    
    
def genTwoLettersAvatar(letter1, letter2):
    font_size = 800
    font_color = getRandomColor()
    bkg_color = '#dddddd'
    image = Image.new('RGBA', (IMAGE_SIZE,IMAGE_SIZE), font_color)
    d = ImageDraw.Draw(image)
    font = ImageFont.truetype("fonts/UbuntuMono-Bold.ttf", font_size)
    d.text((103, 90), letter1.upper()+letter2.upper(), font=font, fill=bkg_color)
    image.show()


if __name__ == "__main__":
    
    
    print(sys.argv)
    
    if(len(sys.argv)>2):
        genTwoLettersAvatar(sys.argv[1][0], sys.argv[2][0])
    else:
        genOneLetterAvatar(sys.argv[1][0])      # first letter of 
    
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
        
    
