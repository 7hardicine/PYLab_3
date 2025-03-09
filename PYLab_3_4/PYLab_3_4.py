import math as m

x0 = float(input("Input the value of x0: "))
xf = float(input("Input the value of x final: "))
dx = float(input("Input the value of step dx: "))

def f1 (x_f):
    f = x_f * m.sqrt(2 - 1.2 * x_f**2)
    return f

def f2 (x_f):
    f = x_f**2 * m.sqrt(2 - 1.2 * x_f)
    return f

x = x0 + dx
d1 = 0
d2 = 0

while xf + dx > x:
    d1 += m.sqrt(dx**2 + (f1(x) - f1(x - dx))**2)
    d2 += m.sqrt(dx**2 + (f2(x) - f2(x - dx))**2)
    print("x =", x, "\nd1 =", d1, "\nd2 =", d2, "\n")
    x += dx
    
if d1 < d2:
    print("The first path is shorter")
else: 
    print("The second path is shorter")