from random import choice
LETTERS = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def getRandomString(length):
    s = ""
    for i in range(length):
        s += choice(LETTERS)
    return s