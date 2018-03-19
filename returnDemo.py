#Caleb Callaway
#3/19/18
#returnDemo.py - how to make functions return a value

#returns random even numbers

from random import randint

def randEven(low,high):
    n=randint(low,high)
    while n%2 !=2:
        n = randint (low,high)
    print (n)
    
randEven(10,20) #test


# print (randint(low/2,high/2)*2)       dun't really work