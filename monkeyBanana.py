#Caleb Callaway
#2/22/18
#monkeyBanana.py- theMonkeyBananaGame



from ggame import *
from random import randint

#constants:
ROWS = 50
COLS = 40
CELLSIZE = 10


def moveRight(event):
    monkey.x += CELLSIZE
    if monkey.x == banana.x and monkey.y == banana.y:
        moveBanana()
    
def moveLeft(event):
    monkey.x -= CELLSIZE
    if monkey.x == banana.x and monkey.y == banana.y:
        moveBanana()
    
def moveDown(event):
    monkey.y += CELLSIZE
    if monkey.x == banana.x and monkey.y == banana.y:
        moveBanana()
    
def moveUp(event):
    monkey.y -= CELLSIZE
    if monkey.x == banana.x and monkey.y == banana.y:
        moveBanana()
    
def moveBanana():
    banana.x = randint(0,COLS-1)*CELLSIZE
    banana.y = randint(0,ROWS-1)*CELLSIZE

if __name__ == "__main__":       #those are 2 underscores not 1      this is so u can run the main part by itself


    green = Color(0x000660,1)
    brown = Color(0x8B4513,1)
    yellow = Color(0XFFFF00,1)

    jungleBox = RectangleAsset(CELLSIZE*COLS,CELLSIZE*ROWS,LineStyle(1,green),green)
    monkeyBody = RectangleAsset(CELLSIZE,CELLSIZE,LineStyle(1,brown),brown)
    bananaBox = RectangleAsset(CELLSIZE,CELLSIZE,LineStyle(2,brown),yellow)
    
    Sprite(jungleBox)
    banana = Sprite(bananaBox,(CELLSIZE*COLS/2,CELLSIZE*ROWS/2))
    monkey = Sprite(monkeyBody)
     
    App().listenKeyEvent('keydown','right arrow', moveRight)
    App().listenKeyEvent('keydown','left arrow', moveLeft)
    App().listenKeyEvent('keydown','down arrow', moveDown)
    App().listenKeyEvent('keydown','up arrow', moveUp)
    App().run()