#Caleb Callaway
#2/22/18
#monkeyBanana.py- theMonkeyBananaGame



from ggame import *
from random import randint

#constants:
ROWS = 50
COLS = 100
CELLSIZE = 10

# moves monkey 1 cell right if possible
def moveRight(event):
    if monkey.x < (COLS-1)*CELLSIZE:
        monkey.x += CELLSIZE
        if monkey.x == banana.x and monkey.y == banana.y:
            moveBanana()
            updateScore()
  
  # moves monkey 1 cell left if possible  
def moveLeft(event):
    if monkey.x>0:
        monkey.x -= CELLSIZE
        if monkey.x == banana.x and monkey.y == banana.y:
            moveBanana()
            updateScore()
    
# moves monkey 1 cell down if possible
def moveDown(event):
    if monkey.y < (ROWS-1)*CELLSIZE:
        monkey.y += CELLSIZE
        if monkey.x == banana.x and monkey.y == banana.y:
            moveBanana()
            updateScore()
            
# moves monkey 1 cell up if possible
def moveUp(event):
    if monkey.y>0:
        monkey.y -= CELLSIZE
        if monkey.x == banana.x and monkey.y == banana.y:
            moveBanana()
            updateScore()
    
# moves banana randomly within constraints
def moveBanana():
    banana.x = randint(0,COLS-1)*CELLSIZE
    banana.y = randint(0,ROWS-1)*CELLSIZE
    
# keeps track of how many frames have happened, runs moveBanana at regular intervals
def step():
    data["frames"] += 1
    if data["frames"]%300 == 0:
        moveBanana()    
    
# increase score and display new text at top right screen, resets timer
def updateScore():
    data["score"]+=10
    data["scoreText"].destroy()                             #remove old writing
    scoreBoard = TextAsset ("Score ="+str(data["score"]))
    data["scoreText"] = Sprite(scoreBoard, (CELLSIZE*COLS - 150,10))
    data["frames"] = 0




#sets up and runs game
if __name__ == "__main__":       #those are 2 underscores not 1      this is so u can run the main part by itself

#holds variables in a dictionary
    data = {}
    data["score"] = 0
    data["frames"] = 0


    green = Color(0x006600,1)
    brown = Color(0x8B4513,1)
    yellow = Color(0XFFFF00,1)
    red = Color(0xFF0000,1)
    black = Color(0X00000000,1)


#graphics
    jungleBox = RectangleAsset(CELLSIZE*COLS,CELLSIZE*ROWS,LineStyle(1,green),green)
    monkeyBody = RectangleAsset(CELLSIZE,CELLSIZE,LineStyle(1,brown),brown)
    bananaBox = RectangleAsset(CELLSIZE,CELLSIZE,LineStyle(2,red),yellow)
    scoreBoard = TextAsset("Score = 0")
    
    Sprite(jungleBox)
    banana = Sprite(bananaBox,(CELLSIZE*COLS/2,CELLSIZE*ROWS/2))
    monkey = Sprite(monkeyBody)
    data["scoreText"] = Sprite(scoreBoard, (CELLSIZE*COLS - 150,10))
     
    App().listenKeyEvent('keydown','right arrow', moveRight)
    App().listenKeyEvent('keydown','left arrow', moveLeft)
    App().listenKeyEvent('keydown','down arrow', moveDown)
    App().listenKeyEvent('keydown','up arrow', moveUp)
    App().run(step)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    