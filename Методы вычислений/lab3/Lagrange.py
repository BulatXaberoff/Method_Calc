import numpy as np
import matplotlib.pyplot as plt


def lagrange(x, x_values, y_values, size: int):
    lag = 0
    for i in range(size):
        basicsPol = 1
        for j in range(size):
            if j != i:
                basicsPol *= (x - x_values[j]) / (x_values[i] - x_values[j])
        lag += basicsPol * y_values[i]
    return lag


def lagranz(x, y, t):
    z = 0
    for j in range(len(y)):
        p1 = 1;
        p2 = 1
        for i in range(len(x)):
            if i == j:
                p1 = p1 * 1;
                p2 = p2 * 1
            else:
                p1 = p1 * (t - x[i])
                p2 = p2 * (x[j] - x[i])
        z = z + y[j] * p1 / p2
    return z

x_arr = np.array([0, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])
y_arr = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18])

x = np.linspace(np.min(x_arr),np.max(x_arr),100)
L_x = []
for i in range(len(x)):
    L_x.append(lagrange(x[i], x_arr, y_arr, len(x_arr)))
plt.plot(x, L_x)
plt.grid(True)
plt.plot(x_arr, y_arr, 'ro')
plt.show()
