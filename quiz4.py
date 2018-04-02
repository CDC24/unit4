#Caleb Callaway
#4/2/18
#quiz4.py - unit quiz



def count(x):
    for i in range (1,x+1):
        print (i)

count(7)  # test of function 1


def excitedPrint(word):
    print (word.upper(),"!!!")
    
excitedPrint("radical")


def firstLetter(letters):
    for ch in letters:
        return ch
        
print (firstLetter("sfrgtbbr"))


def repeats(a,b,c):
    if a==b or b==c or c==a:
        return(True)
    else:
        return(False)
    
print (repeats(5,6,5))