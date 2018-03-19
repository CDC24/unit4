#Caleb Callaway
#3/9/18
#colorChangeWindow.py - uses functions to reprint strings vertically

from ggame import *
from random import randint

red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0X00000000,1)

def randcol():
    gnum = randint (1,4)
    if gnum == 1:
        return (Color(0xFF0000,1))
    elif gnum == 2:
        return (Color(0x00FF00,1))
    elif gnum == 3:
        return (Color(0x0000FF,1))
    elif gnum == 4:
        return (Color(0X00000000,1))


blackOutline = LineStyle(0,black)
redRectangle = RectangleAsset(1500,1000, blackOutline, randcol)


Sprite(redRectangle)

App().listenMouseEvent("click",mouseClick)
App().run()