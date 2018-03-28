#Caleb Callaway
#3/26/18
#printSquares.py - prints squares using functions

def printSquares(rows,cols):
    print("+"+"---+---+"*cols)
    for i in range (0,rows):
        print("|"+"   |   |"*cols)
        print("+"+"---+---+"*cols)
    
printSquares(5,5)