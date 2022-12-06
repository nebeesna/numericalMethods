# Завдання No7
# Знайти наближений розв’язок задачі Коші, використовуючи метод Ейлера
# та один із методів Рунге-Кутта.
# Порівняти точність отриманих розв’язків.
# Обчислити похибку в кінцевій точці відрізку
# Варіант 16

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


def eulers_method(a, b, count, st):
    h = (b - a) / count
    x_r = a
    res = st
    res = res + h * f.evalf(subs={x: x_r, y: res})

    for n in range(1, count):
        x_r = a + n * h
        res = res + h * f.evalf(subs={x: x_r, y: res})
    return res


# 2B
def runge_kutta_method(a, b, count, st):
    h = (b - a) / count
    x_r = a
    res = st

    for n in range(0, count):
        x_r = a + n * h
        k1 = h * f.evalf(subs={x: x_r, y: res})
        k2 = h * f.evalf(subs={x: x_r + h/2, y: res + k1/2})
        res += k2
    return res


# count = int(input('Введіть к-сть поділів: '))
# k = 1
# print('метод Ейлера:')
# res_accurate = sympify(F.evalf(subs={x: b}))
# print(f'Точний розв\'язок: {res_accurate}')
# while k < 5:
#     print(f'{count=}')
#     res = eulers_method(a, b, count, st)
#     print(f'розв\'язок: {res}')
#     p = abs(res_accurate - res)
#     print(f"Похибка: {p}")
#
#     k += 1
#     count *= 10
#
# count = int(input('\n\nВведіть к-сть поділів: '))
# k = 1
# print('\n\nметод Рунге-Кутта:')
# print(f'Точний розв\'язок: {res_accurate}')
# while k < 5:
#     print(f'{count=}')
#     res = runge_kutta_method(a, b, count, st)
#     print(f'розв\'язок: {res}')
#     p = abs(res_accurate - res)
#     print(f"Похибка: {p}")
#
#     k += 1
#     count *= 10
c = int(4)
res = runge_kutta_method(a, b, c, st)
print(res)
