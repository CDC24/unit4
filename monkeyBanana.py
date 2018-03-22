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
    if monkey.x < (COLS-1)*CELLSIZE:
        monkey.x += CELLSIZE
        if monkey.x == banana.x and monkey.y == banana.y:
            moveBanana()
            data["score"]+= 3.14159265359
            print (data["score"])
    
def moveLeft(event):
    if monkey.x>0:
        monkey.x -= CELLSIZE
        if monkey.x == banana.x and monkey.y == banana.y:
            moveBanana()
            data["score"]+= 3.14159265359
            print (data["score"])
    
def moveDown(event):
    if monkey.y < (ROWS-1)*CELLSIZE:
        monkey.y += CELLSIZE
        if monkey.x == banana.x and monkey.y == banana.y:
            moveBanana()
            data["score"]+= 3.14159265359
            print (data["score"])
    
def moveUp(event):
    if monkey.y>0:
        monkey.y -= CELLSIZE
        if monkey.x == banana.x and monkey.y == banana.y:
            moveBanana()
            data["score"]+= 3.14159265359
            print (data["score"])
    
def moveBanana():
    banana.x = randint(0,COLS-1)*CELLSIZE
    banana.y = randint(0,ROWS-1)*CELLSIZE

if __name__ == "__main__":       #those are 2 underscores not 1      this is so u can run the main part by itself

#hold variables in a dictionary
    data = {}
    data["score"] = 0


    green = Color(0x006600,1)
    brown = Color(0x8B4513,1)
    yellow = Color(0XFFFF00,1)
    red = Color(0xFF0000,1)
    black = Color(0X00000000,1)

    jungleBox = RectangleAsset(CELLSIZE*COLS,CELLSIZE*ROWS,LineStyle(1,black),black)
    monkeyBody = RectangleAsset(CELLSIZE,CELLSIZE,LineStyle(1,brown),brown)
    bananaBox = RectangleAsset(CELLSIZE,CELLSIZE,LineStyle(2,red),yellow)
    
    Sprite(jungleBox)
    banana = Sprite(bananaBox,(CELLSIZE*COLS/2,CELLSIZE*ROWS/2))
    monkey = Sprite(monkeyBody)
     
    App().listenKeyEvent('keydown','right arrow', moveRight)
    App().listenKeyEvent('keydown','left arrow', moveLeft)
    App().listenKeyEvent('keydown','down arrow', moveDown)
    App().listenKeyEvent('keydown','up arrow', moveUp)
    App().run()