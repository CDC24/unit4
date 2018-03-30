#Caleb Callaway
#3/29/18
#triangle.py - finds the area of a triangle


from math import sqrt

def distance(x1,y1,x2,y2):
    return(sqrt((x2-x1)**2+(y2-y1)**2))
    
x1 = int(input("x1= "))  
y1 = int(input("y1= "))  
x2 = int(input("x2= "))  
y2 = int(input("y2= "))  
x3 = int(input("x3= "))  
y3 = int(input("y3= "))


def triangle(x1,y1,x2,y2,x3,y3):
    a= distance(x1,y1,x2,y2)
    b= distance(x2,y2,x3,y3)
    c= distance(x3,y3,x1,y1)
    s= (0.5*(a+b+c))
    return (sqrt(s*(s-a)*(s-b)*(s-c)))

print(triangle(x1,y1,x2,y2,x3,y3))

"""
print(triangle(3,4,-5,2,-7,1))
"""



