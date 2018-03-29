#Caleb Callaway
#3/28/18
#stringUnion.py - blends two words


def stringUnion(word1,word2):
    twoword=("word1"+"word2")
    newword=("")
    for ch in twoword:
        if ch not in newword:
            newword +=(ch)
    return(newword)
            
            
print(stringUnion("Mississippi","Pensylvania"))