import math as m

TaskSolv = lambda x_solv, y_solv: m.tan(x_solv + y_solv) - m.sqrt(m.fabs(x_solv**2 - y_solv**2))

x = float(input("Input the value of x1: "))
y = float(input("Input the value of y1: "))

f = TaskSolv(x, y)
print("The value of function, where x =", x, "y =", y, "is", f)

x = float(input("Input the value of x2: "))
y = float(input("Input the value of y2: "))

f = TaskSolv(x, y)
print("The value of function, where x =", x, "y =", y, "is", f)