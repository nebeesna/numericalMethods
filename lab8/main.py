from sympy import symbols, sqrt, exp, sympify

x, y = symbols('x y')
# у'
f = x * y * (y ** 2 - 1)
# y(0) = 0.5
st = 0.5
# у*
F = 1 / (sqrt(3 * exp(x ** 2) + 1))
# [0,1]
a = 0
b = 1
eps = 0.00001


def adams_method(a, b, st, m, f, eps):
    h = (b - a) / m
    us1 = 0
    us = 0
    un = st
    for i in range(0, m):
        us = un + h*f.evalf(subs={x: a + h * i, y: un})
        f1 = f.evalf(subs={x: a + h * (i + 1), y: us})
        f2 = f.evalf(subs={x: a + h * i, y: un})
        us1 = un + h*(f1 + f2)/2

        while abs(us1 - us) >= eps:
            us = us1
            f1 = f.evalf(subs={x: a + h * (i + 1), y: us})
            f2 = f.evalf(subs={x: a + h * i, y: un})
            us1 = un + h*(f1 + f2)/2
        un = us1
    return us1


m = int(10)
k = 1
print('метод Адамса:')
res_accurate = sympify(F.evalf(subs={x: b}))
print(f'Точний розв\'язок: {res_accurate}')
while k < 4:
    print(f'{m=}')
    res = adams_method(a, b, st, m, f, eps)
    print(f'розв\'язок: {res}')
    p = abs(res_accurate - res)
    print(f"Похибка: {p}")

    k += 1
    m *= 10

