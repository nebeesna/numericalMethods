import numpy as np


def norma_of(a):
    norma = 0
    for i in range(len(a)):
        sum = 0
        for j in range(len(a[i])):
            sum += abs(a[i][j])
        if sum > norma:
            norma = sum
    return norma


def method_yakobi(a, b, e):
    for i in range(len(a)):
        z = -a[i][i]
        a[i][i] = 0
        b[i] /= -z
        for j in range(len(a[i])):
            if i != j:
                a[i][j] /= z
    print("C:")
    print(a)
    print("b:")
    print(b)
    norma_c = norma_of(a)
    print(f"||C|| = {norma_c}")
    if norma_c < 1:
        xk = b.copy()
        k = 0
        xk1 = a.dot(xk) + b
        print(f"наближення x({k})")
        print(xk1)
        while norma_of(xk1 - xk) > ((1 - norma_c) * e / norma_c):
            xk = xk1
            xk1 = a.dot(xk) + b
            k += 1
            print(f"наближення x({k})")
            print(xk1)

        print("розв'язок рівняння:")
        print(xk1)

    else:
        print("Matrix's norma is more than 1")


a = np.array([[-0.86, 0.23, 0.18, 0.17],
              [0.12, -1.14, 0.08, 0.09],
              [0.16, 0.24, -1, -0.35],
              [0.23, -0.08, 0.05, -0.75]])
print("a:")
print(a)
e = 0.0001
b = np.array([[1.42], [0.83], [-1.21], [-0.65]])
print("b:")
print(b)
method_yakobi(a, b, e)


