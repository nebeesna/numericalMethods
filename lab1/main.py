import math

x = []
print("f(x) = 5x - 8lgx - 8 = 0")
print("Введіть бажаний проміжок:")

a = float(input("a= "))
b = float(input("b= "))

e = 0.000001

print("точність: " + str(e))

min_zn = 8 / (5*math.log(10))

aY = 5*a - 8*math.log10(a) - 8
bY = 5*b - 8*math.log10(b) - 8

if a != min_zn and b != min_zn:
    if bY > aY:
        x.append(b)
        x.append(a)
    elif aY > bY:
        x.append(a)
        x.append(b)

while abs(x[len(x)-1] - x[len(x)-2]) >= e:
    xn = x[len(x)-1]
    t = xn - ((xn - x[0])/(5*xn - 8 * math.log10(xn) - 8 - 5*x[0] + 8*math.log10(x[0]) + 8)) * \
        (5*xn - 8 * math.log10(xn) - 8)
    x.append(t)

print("Розв'язок = " + str(x[len(x)-1]))
















