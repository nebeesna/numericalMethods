from sympy import *
# завдання 5
# варіант 16
# 1/(х3+х+1)
# Ньютона вперед для нерівновіддалених вузлів
# а = 1.0
# б = 2.0
# На вiдрiзку [a,b] вибрано систему вузлів xі
# в яких відомі значення функції fi = f (xi).
# Користуючись інтерполяційними поліномами (*) обчислити значення функції
# f*(x) в деякій точці x* ∈ [a,b] з заданою точністю ε.
# вивести:
# - кількість членів в інтерполяційній формулі,
# - похибку D = |f(x*)- f*(x*)|
x = Symbol('x')
# f = 1 / (x**3 + x + 1)
f = x**4 + 1
# x_values = [1.0, 1.12, 1.3, 1.46, 1.62, 1.74, 1.88, 2.0]
# y_values = [f.subs(x, i) for i in x_values]
x_values = [1.0, 1.34, 1.87, 2.0]
y_values = [f.subs(x, i) for i in x_values]

def divided_difference(i_s, i_f):
    x_t = 1
    res = 0
    for i in range(i_s, i_f + 1):
        for j in range(i_s, i_f + 1):
            if j != i:
                x_t *= (x_values[i] - x_values[j])
        res += y_values[i] / x_t
        x_t = 1
    return res

def interpolation_polynom():
    res = y_values[0]
    x_t = 1
    t = 1
    for i in range(1, len(x_values)):
        for j in range(0, t):
                x_t *= (x - x_values[j])
        res += x_t * divided_difference(0, i)
        x_t = 1
        t += 1
    return res


Ln = interpolation_polynom()

x_r = input("x* = ")
print(f"f*({x_r}) = {Ln.subs(x, x_r)}")
print(f"кількість членів в інтерполяційній формулі {len(x_values)}")
print(f"похибкa D = |f(x*)- f*(x*)| = {abs(f.subs(x, x_r) - Ln.subs(x, x_r))}")