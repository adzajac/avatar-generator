from random import randint, random
import colorsys

def hex_to_rgb(h):
    ''' takes hex in format: #ffffff ; returns tuple of three (r,g,b) '''
    return tuple([int(i,16)/256 for i in [h[1:3], h[3:5], h[5:7]]])


def rgb_to_hex(rgb):
    ''' takes tuple (r,g,b), returns in hex format #ffffff '''
    return "#{:02x}{:02x}{:02x}".format(int(rgb[0]*256),int(rgb[1]*256),int(rgb[2]*256))
    
    
def getRandom():
    h = random()
    s = 0.41
    v = 0.61
    return rgb_to_hex(colorsys.hsv_to_rgb(h,s,v))


def makeHexDarker(color_hex):
    r,g,b = hex_to_rgb(color_hex)
    h,s,v = colorsys.rgb_to_hsv(r,g,b)
    h,s,v = makeHSVDarker(h,s,v)
    return rgb_to_hex(colorsys.hsv_to_rgb(h,s,v))


def makeHSVDarker(h,s,v):   
    return h,s,max(v-0.1, 0)    # making it darker, but making sure not to get negative number
