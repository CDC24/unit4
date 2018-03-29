#Caleb Callaway
#3/29/18
#recursionDemo.py - recursive version of countdown


def countdownr(n):
    if n == 0:                 # establishes 'base case'
        print("KERCHOW!")
    else:                      # recursive step- calls itself
        print (n)
        countdownr(n-1)
        
        
countdownr(5)
