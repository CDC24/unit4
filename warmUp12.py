#Caleb Callaway
#3/29/18
#warmUp12.py - finds gcf of two numbers



def GCF(num1,num2):
    if num1 > num2:                     #You don't actually need this part;
        smaller = num2
    else:
        smaller = num1
    for i in range (smaller,0,-1):      #Just write 'num1' or 'num2' here instead of smaller
        if num1%i==0 and num2%i==0:
            return (i)

print (GCF(12,15))
print (GCF(5,9))
print (GCF(16,64))