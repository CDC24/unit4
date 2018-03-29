#Caleb Callaway
#3/28/18
#stringIntersect.py - prints the letters appearing in both of two words

def stringIntersect(word1,word2):
    newword=("")
    for ch in word1:
        if ch.lower()in word2:
            newword +=(ch.lower())
    return(newword)
            
            
print(stringIntersect("Mississippi","Pensylvania"))
