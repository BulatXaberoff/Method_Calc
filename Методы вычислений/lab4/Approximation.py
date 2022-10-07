import numpy as np
import matplotlib.pyplot as plt


def f(x_r):
    return X[0] * x_r ** 2 + X[1] * x_r + X[2]


def f_1(x_r):
    return X_1[0] + X_1[1] * x_r


x = np.array([0, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])
y = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18])
n = len(x)
s1 = np.sum(x)
s2 = np.sum(x ** 2)
s3 = np.sum(x ** 3)
s4 = np.sum(x ** 4)
s5 = np.sum(x ** 2 * y)
s6 = np.sum(x * y)
s7 = np.sum(y)

# print(f"{s1} {s2} {s3} {s4}")
A = np.array([[s4, s3, s2],
              [s3, s2, s1],
              [s2, s1, n]])
b = np.array([s5, s6, s7])
print(f"{A}       {np.array(b)}")
X = np.linalg.solve(A, b)
print(f"a*x_2^2 + b*x_1 + c")
print(f"{X[0]}*x_2^2 + {X[1]}*x_1 + {X[2]}")
print("Подставим в полученную функцию\n"
      f"{X}")
res = f(x)
print(res)

x_other = np.linspace(-100, 100)
plt.plot(x, y, 'ro')
plt.plot(x_other, f(x_other))
plt.grid(True)
plt.title('Квадратичная аппроксимация')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
A_1 = np.array([[n, s1], [s1, s2]])
b_1 = np.array([s7, s6])
X_1 = np.linalg.solve(A_1, b_1)
plt.plot(x, y, 'ro')
plt.plot(x_other, f_1(x_other))
plt.grid(True)
plt.title('Линейная аппроксимация')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
