#Caleb Callaway
#3/9/18
#printStars.py - uses functions to print stars


def printStars(e):
    for i in range(1,  e+1):
       print (" "*(e-i)," *"*i)
       
e = int(input("Enter a number "))

printStars(e)
