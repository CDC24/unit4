#Caleb Callaway
#3/9/18
#colorChangeWindow.py - uses functions to reprint strings vertically

from ggame import *

red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0X00000000,1)

blackOutline = LineStyle(1,black)
redRectangle = RectangleAsset(1000,1000, blackOutline, red)


Sprite(redRectangle)


App().run()