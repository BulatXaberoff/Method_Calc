import numpy as np


def iterations_SLU(A, b, n,eps):
    Alpha = np.empty((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                Alpha[i, j] = -A[i, j] / A[i, i]
            else:
                Alpha[i, j] = 0
    betta = b / A.diagonal()
    x = betta
    x1 = betta + Alpha @ x
    while (abs(x - x1) > eps).any():
        x = betta + Alpha @ x1
        x1 = betta + Alpha @ x
    return x1


def system_equal(x1, x2):
    return np.array([[np.cos(x2 - 2), x1],
                     [x2, np.sin(x1 + 0.5)]])


def iterations_SLU_1(eps):
    # x, x1 = [0.1,0.1], [0.1,0.1]
    # while (np.abs(system_equal(x[0], x[1]) - b) > eps).any():
    #     A = system_equal(x[0],x[1])
    #     print(np.abs(system_equal(x[0], x[1]) - b))
    #     Alpha = np.empty((n, n))
    #     for i in range(n):
    #         for j in range(n):
    #             if i != j:
    #                 Alpha[i, j] = -A[i, j] / A[i, i]
    #             else:
    #                 Alpha[i, j] = 0
    #     betta = b / A.diagonal()
    #     x = betta
    #     x1 = betta + Alpha @ x
    #     while (np.abs(system_equal(x[0], x[1]) - b) > eps).any():
    #         x = betta + Alpha @ x1
    #         x1 = betta + Alpha @ x
    x1 = x2 = 0
    n = 0
    x1_v = -np.cos(x2 - 2)
    x2_v = 1 - np.sin(x1 + 1 / 2)
    n += 1
    while (np.abs(x1_v - x1) > eps) and np.abs(x2_v - x2) > eps:
        x1_v = -np.cos(x2 - 2)
        x2_v = 1 - np.sin(x1 + 1 / 2)
        x1 = -np.cos(x2_v - 2)
        x2 = 1 - np.sin(x1_v + 1 / 2)
        n += 1

    res=x1+np.cos(x2-2)
    res1=np.sin(x1+1/2)+x2-1
    print(f"Решение системы {x1} {x2}\n"
          f"Подставим обратно в систему и получим приближенное равенство:")
    print("x1+cos(x2-2)=0\n"
          "sin(x1+1/2)+x2=1\n"
          f"{res} {res1}")







#
print(f'Дано матричное уравнение вида Ax=b, где')
eps = 0.001
A = np.array([[1, 5, -3],
              [1, -1, 5],
              [8, 1, 1]])
A_p = np.array([[5, -3, 1],
                [-1, 5, 1],
                [1, 1, 8]])
b = np.array([7, 7, 26])
print(f"Матрица A:\n"
      f"{A}\n"
      f"x - неизвестные\n"
      f"Вектор столбец b:\n{b}")

# f"Приведенная матрица A_p:\n"
#       f"{A_p}\n"
res = iterations_SLU(A_p, b, A_p.shape[0],eps)
print(f"Решение уравнения:{res}")

print("Подставим обратно в систему и получим приближенное равенство:\n"
      "AX-b=0\n"
      f"{A_p @ res - b}")
input("\n\nНажмите пробел")
iterations_SLU_1(0.001)

