import math as m

def POfTriangle ():
    a = int(input("Input the value of a: "))
    b = int(input("Input the value of b: "))
    c = int(input("Input the value of c: "))
    P = a + b + c
    print("The value of P =", P, "\n")

def POfFoundPrism ():
    x = int(input("Input count of sides: "))
    P = 0
    for i in range (0, x):
        P += int(input("Input the value of side: "))
    print("The value of P =", P, "\n")

def POfFoundCylinder ():
    r = int(input("Input the value of r: "))
    P = 2 * m.pi * r
    print("The value of P =", P, "\n")
