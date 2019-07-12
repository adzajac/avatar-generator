from PIL import ImageFont, ImageDraw, Image

import argparse

def genOneLetterAvatar(letter):
    image_size = 1024
    font_size = 1228 
    font_color = '#550000'
    bkg_color = '#dddddd'
    image = Image.new('RGBA', (image_size,image_size), font_color)
    d = ImageDraw.Draw(image)
    font = ImageFont.truetype("fonts/UbuntuMono-Bold.ttf", font_size)
    d.text((203, -128), letter.upper(), font=font, fill=bkg_color)
    image.show()
    
    
def genTwoLettersAvatar(letter1, letter2):
    print("not yet ready")
    print("letters: {} and {}".format(letter1, letter2))


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--l1',
        help='first letter of the avatar',
        default ='A',
        required=True
    )
    parser.add_argument(
        '--l2',
        help='second letter of the avatar',
        default =''
    )
    args = parser.parse_args()
    
    
    if not args.l2:
        genOneLetterAvatar(args.l1)
    else:
        genTwoLettersAvatar(args.l1, args.l2)
        
    
