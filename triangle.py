#Caleb Callaway
#3/29/18
#triangle.py - finds the area of a triangle


from math import sqrt

def triangle(x1,y1,x2,y2,x3,y3):
    a= (sqrt((x2-x1)**2+(y2-y1)**2))
    b= (sqrt((x3-x2)**2+(y3-y2)**2))
    c= (sqrt((x1-x3)**2+(y1-y3)**2))
    s= (0.5*(a+b+c))
    return (sqrt(s(s-a)(s-b)(s-c)))
