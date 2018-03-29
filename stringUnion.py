#Caleb Callaway
#3/28/18
#stringUnion.py - blends two words


def stringUnion(word1,word2):
    twoword=(word1+word2)
    newword=("")
    for ch in twoword:
        if ch.lower() not in newword.lower():
            newword +=(ch.lower())
    return(newword)
            
            
print(stringUnion("Mississippi","Pensylvania"))