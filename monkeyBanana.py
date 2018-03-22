#Caleb Callaway
#2/22/18
#monkeyBanana.py- theMonkeyBananaGame



from ggame import *

#constants:
ROWS = 30
COLS = 70
CELLSIZE = 20


def moveRight(event):
    monkey.x += CELLSIZE
    
def moveLeft(event):
    monkey.x -= CELLSIZE
    
def moveDown(event):
    monkey.y += CELLSIZE
    
def moveUp(event):
    monkey.y -= CELLSIZE

if __name__ == "__main__":       #those are 2 underscores not 1      this is so u can run the main part by itself


    green = Color(0x000660,1)
    brown = Color(0x8B4513,1)
    yellow = Color(0XFFFF00,1)

    jungleBox = RectangleAsset(CELLSIZE*COLS,CELLSIZE*ROWS,LineStyle(1,green),green)
    monkeyBody = RectangleAsset(CELLSIZE,CELLSIZE,LineStyle(1,brown),brown)
    bananaBox = RectangleAsset(CELLSIZE,CELLSIZE,LineStyle(2,brown),yellow)
    
    Sprite(jungleBox)
    monkey = Sprite(monkeyBody)
    banana = Sprite(bananaBox(CELLSIZE*COLS/2,CELLSIZE*ROWS/2))
    
    App().listenKeyEvent('keydown','right arrow', moveRight)
    App().listenKeyEvent('keydown','left arrow', moveLeft)
    App().listenKeyEvent('keydown','down arrow', moveDown)
    App().listenKeyEvent('keydown','up arrow', moveUp)
    App().run()