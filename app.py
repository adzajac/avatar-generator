from PIL import ImageFont, ImageDraw, Image


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
    
    
genOneLetterAvatar('A')
