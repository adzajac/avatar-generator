from PIL import ImageFont, ImageDraw, Image


def genOneLetterAvatar(letter):
    img_size = 1024
    font_size = 1228
    image = Image.new('RGBA', (img_size,img_size), (255,255,255,256))
    d = ImageDraw.Draw(image)
    font = ImageFont.truetype("fonts/UbuntuMono-Bold.ttf", font_size)
    d.text((203, -128), letter.upper, font=font, fill=(0,0,0,256))
    image.show()
    

genOneLetterAvatar('A')
