#Caleb Callaway
#4/2/18
#quiz4.py - unit quiz



def count(x):                           # function 1
    for i in range (1,x+1):
        print (i)

count(7)                                # test of function 1


def excitedPrint(word):                 # function 2
    print (word.upper(),"!!!")
    
excitedPrint("radical")                 # test of function 3


def firstLetter(letters):               # function 3
    for ch in letters:
        return ch
        
print (firstLetter("sfrgtbbr"))         # test of function 3


def repeats(a,b,c):                     # function 4
    if a==b or b==c or c==a:
        return(True)
    else:
        return(False)
    
print (repeats(5,6,5))                  # test of function 4