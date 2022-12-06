from sympy import *
# варіант 16
# cos(y - 1) + x= 0.5
# y - cos(x) = 3
# метод простої ітерації

e = 0.00001
x_k1 = 0.9
y_k1 = 3.622

k = 1

while True:
    x_k = x_k1
    y_k = y_k1
    x_k1 = 0.5 - cos(y_k-1)
    y_k1 = 3 + cos(x_k)
    print(f"№{k}   x = {x_k1}   y = {y_k1}")
    k += 1

    if (abs(max(x_k1 - x_k, y_k1 - y_k)))/abs(max(x_k, y_k)) < e:
        break

print("\nШуканий наближений розв'язок: ")
print(f"x = {x_k1}   y = {y_k1}")
print("(метод простої ітерації)")
