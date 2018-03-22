#Caleb Callaway
#2/22/18
#monkeyBanana.py- theMonkeyBananaGame



from ggame import *

#constants:
ROWS = 40
COLS = 80
CELLSIZE = 20


if __name__ == "__main__":       #those are 2 underscores not 1      this is so u can run the main part by itself


    green = Color(0x000660,1)
    brown = Color(0x8B4513,1)
    yellow = Color(0X00000000,1)

    jungleBox = RectangleAsset(CELLSIZE*COLS,CELLSIZE*ROWS,LineStyle(1,green),green)
    monkey = RectangleAsset(CELLSIZE,CELLSIZE,LineStyle(1,brown),brown)


    Sprite(jungleBox)
    Sprite(monkey)

    App().run()