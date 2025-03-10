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

def Menu ():
    IsExitMenu = 0
    print("Calculate the perimeter\n1. Of Triangle\n2. Of Found Prism\n3. Of Found Cylinder\n4. Exit\n")
    MenuSelection = input()
    if MenuSelection == '1':
        POfTriangle()
    elif MenuSelection == '2':
        POfFoundPrism()
    elif MenuSelection == '3':
        POfFoundCylinder()
    elif MenuSelection == '4':
        IsExitMenu = 1
    else:
        print("Something went wrong, please try again:\n")
    return IsExitMenu

IsExit = 0

while IsExit == 0:
    IsExit = Menu()

