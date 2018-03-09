#Caleb Callaway
#3/9/18
#countdown.py - uses functions to count down



def countdown(num):
    for i in range (-num, 0):
    print (-i)
    if i == -1:
        print ("BOOOM! GOT 'EM")
        
q = int(input("Enter a number: "))

countdown (q)