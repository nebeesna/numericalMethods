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


def method_zejdelia(a, b, e):
    dd = np.zeros((4, 4))
    du = np.zeros((4, 4))
    for i in range(len(a)):
        z = -a[i][i]
        for j in range(len(a[i])):
            if i > j:
                dd[i][j] = a[i][j] / z
            if i < j:
                du[i][j] = a[i][j] / z


    print("D нижня:")
    print(dd)
    print("D верхня:")
    print(du)
    norma_c = norma_of(du + dd)
    print("C = Dнижня + Dверхня")
    print(f"||C|| = {norma_c}")
    if norma_c < 1:
        xk0 = b
        for i in range(0, len(b)):
            xk0[i] /= a[i][i]
        k = 0
        xk1 = xk0
        x = dd.dot(xk1) + du.dot(xk0) + b
        print(f"наближення x({k})")
        print(x)
        while norma_of(x - xk1) > ((1 - norma_c) * e / norma_c):
            xk0 = xk1
            xk1 = x
            x = dd.dot(xk1) + du.dot(xk0) + b
            k += 1
            print(f"наближення x({k})")
            print(x)

        print("розв'язок рівняння:")
        print(x)

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
method_zejdelia(a, b, e)


