from sympy import *
import numpy as np
from numpy import linalg

# варіант 16
# cos(y - 1) + x= 0.5
# y - cos(x) = 3
# метод ньютона
e = 0.00001
x, y = symbols('x y')
f1 =2*x**2 - 3*y**2 - 20
f2 = x*y - y**2 - 4
x_k1 = 3
y_k1 =1

xy_k1 = np.array([x_k1, y_k1])

fx_1 = diff(f1, x)
fx_2 = diff(f1, y)
fx_3 = diff(f2, x)
fx_4 = diff(f2, y)

k = 1
print(fx_1)
print(fx_2)
print(fx_3)
print(fx_4)
while True:
    xy_k = xy_k1.copy()

    fx_k = np.array([[float(fx_1.subs([(x, x_k1), (y, y_k1)])), float(fx_2.subs([(x, x_k1), (y, y_k1)]))],
                     [float(fx_3.subs([(x, x_k1), (y, y_k1)])), float(fx_4.subs([(x, x_k1), (y, y_k1)]))]])
    print(fx_k)
    if np.linalg.det(fx_k) == 0:
        print("determinant = 0")
        break

    fx_k = linalg.inv(fx_k)
    print(fx_k)

    f_k = np.array([[float(f1.subs([(x, x_k1), (y, y_k1)])),
                     float(f2.subs([(x, x_k1), (y, y_k1)]))]])
    print(f_k)
    mult = np.array([fx_k[0][0] * f_k[0, 0] + fx_k[0][1] * f_k[0, 1],
                    fx_k[1][0] * f_k[0, 0] + fx_k[1][1] * f_k[0, 1]])
    print(mult)

    xy_k1 = xy_k - mult
    x_k1 = xy_k1[0]
    y_k1 = xy_k1[1]
    print(f"№{k}   x = {xy_k1[0]}   y = {xy_k1[1]}")
    k += 1
    if (linalg.norm(xy_k1 - xy_k)) / linalg.norm(xy_k1) < e:
        break

print("\nШуканий наближений розв'язок: ")
print(f"x = {xy_k1[0]}   y = {xy_k1[1]}")
print("(метод Ньютона)")
