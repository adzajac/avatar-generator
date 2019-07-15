#import sys
#sys.path = ['.'] + sys.path

from flask import Flask

import avatargenerator as avgen



app = Flask(__name__)




if __name__ == "__main__":
    print("example")

    avgen.generateLetterAvatar('a','c', size=128)
    avgen.generateLetterAvatar('a','c', size=256)
    avgen.generateLetterAvatar('a','c', size=512)
    