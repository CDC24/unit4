#Caleb Callaway
#3/29/18
#stringIntersect.py - prints the letters appearing in both of two words

def stringIntersect(word1,word2):
    newword=("")
    for ch in word1.lower():
        if ch.lower()in word2.lower() and ch.lower() not in newword:
            newword +=(ch.lower())
    return(newword)
            
            
print(stringIntersect("Mississippi","Pensylvania"))
