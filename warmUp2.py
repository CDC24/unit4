#Caleb Callaway
#3/26/18
#warmUp2.py

# function that returns true if a number is prime and false otherwise


def prime(num):
    for i in range (2, num):
        if num%i==0:
            return (False)
        else:
            return(True)

    
    
    
num = int(input("Enter a number: "))

print (prime(num))