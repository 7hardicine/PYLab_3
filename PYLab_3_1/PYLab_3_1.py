import math as m

def Output (P):
    print("The value of P =", P, "\n")

def POfTriangle ():
    a = int(input("Input the value of a: "))
    b = int(input("Input the value of b: "))
    c = int(input("Input the value of c: "))
    P = a + b + c
    Output(P)

def POfFoundPrism ():
    x = int(input("Input count of sides: "))
    P = 0
    for i in range (0, x):
        P += int(input("Input the value of side: "))
    Output(P)

def POfFoundCylinder ():
    r = int(input("Input the value of r: "))
    P = 2 * m.pi * r
    Output(P)

IsExit = 0

while IsExit == 0:

    print("Calculate the perimeter\n1. Of Triangle\n2. Of Found Prism\n3. Of Found Cylinder\n4. Exit\n")

    MenuSelection = int(input())
    if MenuSelection == 1:
        POfTriangle()
    elif MenuSelection == 2:
        POfFoundPrism()
    elif MenuSelection == 3:
        POfFoundCylinder()
    else:
        IsExit = 1
