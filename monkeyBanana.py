#Caleb Callaway
#2/22/18
#monkeyBanana.py- theMonkeyBananaGame



from ggame import *

#constants:
ROWS = 20
COLS = 40
CELLSIZE = 20


if __name__ == "__main__":       #those are 2 underscores not 1      this is so u can run the main part by itself


    green = Color(0x006600,1)
    brown = Color(0x0000FF,1)
    yellow = Color(0X00000000,1)

    jungleBox = RectangleAsset(CELLSIZE*COLS,CELLSIZE*ROWS,LineStyle(1,green),green)

    Sprite(jungleBox)

    App().run()