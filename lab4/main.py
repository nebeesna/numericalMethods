from sympy import Symbol
import matplotlib.pyplot as plt
# Завдання №4
# Побудувати інтерполяційний многочлен Лагранжа та за його допомогою
# знайти наближене значення функції у вказаній точці. Вивести його графік.
# Варіант 16

x = Symbol('x')
x_initial = [0, 0.75, 1.6, 2.36, 3.75]
y_initial = [3, 2.8, 3.7, 3.5, 4]
# x_initial = [-1, 0, 1, 3]
# y_initial = [0, 1, 2, 28]

# x_final = 2.6
x_final = 2

def polunom_lagtange():
    lnx = 0
    for i in range(len(x_initial)):
        x_xi = y_initial[i]
        for j in range(len(x_initial)):
            if i != j:
                x_xi *= (x - x_initial[j]) / (x_initial[i] - x_initial[j])
        lnx += x_xi
    return lnx

lnx = polunom_lagtange()
y_final = lnx.subs(x, x_final)

a = min(x_initial)
b = max(x_initial)
g_x = []
g_y = []

while a <= b:
    g_x.append(a)
    g_y.append(lnx.subs(x, a))
    a += 0.01

print(f"f({x_final}) = {y_final}")
plt.grid()
plt.xlabel(f"f({x_final}) = {round(y_final, 5)}", fontsize=12)
plt.plot(g_x, g_y, color='#3c887e')
plt.scatter(x_final, y_final, color='#3c887e')
plt.show()
