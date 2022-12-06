from sympy import Symbol, sin, cos, log
# Variant 16
# Використовуючи квадратурні формули прямокутників, трапецій та парабол,
# обчислити інтеграли від заданих функцій із заданою точністю .
# Для досягнення точності  подрібнювати  крок  розбиття  вихідного  проміжку h.
# Вивести,  крім обчисленого інтегралу,кількість ітерацій по кожній квадратурній формулі
# та порядок збіжності квадратурної формули
# k = ln((ih - ih-2)/(ih-2 - ih-4)) / ln2
# Порівняти обчислений  інтеграл з  точним  значенням,  використовуючи відому первісну F(x)
x = Symbol('x')
f = x * sin(x)
F = sin(x) - x * cos(x)
a = 1
b = 2
eps = 0.00001
basic_res = float(F.subs(x, b) - F.subs(x, a))

def quadrature_formula_of_rectangles(f, a, b, eps):
    n = 1
    h = b - a
    res = h * (f.subs(x, (a + h / 2)))
    res = float(res)
    k = 1
    while abs(res - basic_res) > eps:
        k += 1
        n += 1
        h = (b - a) / n
        res = 0
        for i in range(1, n + 1):
            res += f.subs(x, (a + (2 * i - 1) * (h / 2)))
        res *= h
        res = float(res)

    p = log((res*h - res*h/2) / (res*h/2 - res*h/4)) / log(2)
    print("\nМетод прямокутника:")
    print(f"{basic_res=}")
    print(f"{res=}")
    print(f"Кількість ітерацій = {k}")
    print(f"Порядок = {float(p)}")
    return res

def quadrature_formula_of_trapezoids(f, a, b, eps):
    n = 1
    h = b - a
    k = 1
    res = h * (f.subs(x, a) + f.subs(x, b)) / 2
    res = float(res)
    while abs(res - basic_res) > eps:
        k += 1
        n += 1
        h = (b - a) / n
        res = 0
        for i in range(1, n):
            res += f.subs(x, (a + i * h))
        res += (f.subs(x, a) + f.subs(x, b))/2
        res *= h
        res = float(res)

    p = log((res*h - res*h/2) / (res*h/2 - res*h/4)) / log(2)
    print("\nМетод трапеції:")
    print(f"{basic_res=}")
    print(f"{res=}")
    print(f"Кількість ітерацій = {k}")
    print(f"Порядок = {float(p)}")
    return res

def quadrature_formula_of_parabolas(f, a, b, eps):
    n = 2
    h = (b - a) / 2
    k = 0
    res = (h / 3) * (f.subs(x, a) + 4 * f.subs(x, (a + b)/2) + f.subs(x, b))
    res = float(res)
    while abs(res - basic_res) > eps:
        k += 1
        n += 1
        res = 0
        h = (b - a) / n
        x0 = a + h
        for i in range(1, n):
            if i % 2 == 0:
                res += 2 * f.subs(x, x0)
            if i % 2 == 1:
                res += 4 * f.subs(x, x0)
            x0 += h
        res += f.subs(x, a) + f.subs(x, b)
        res *= h / 3
        res = float(res)

    p = log((res*h - res*h/2) / (res*h/2 - res*h/4)) / log(2)
    print("\nМетод парабол:")
    print(f"{basic_res=}")
    print(f"{res=}")
    print(f"Кількість ітерацій = {k}")
    print(f"Порядок = {float(p)}")
    return res


quadrature_formula_of_rectangles(f, a, b, eps)
quadrature_formula_of_trapezoids(f, a, b, eps)
quadrature_formula_of_parabolas(f, a, b, eps)
