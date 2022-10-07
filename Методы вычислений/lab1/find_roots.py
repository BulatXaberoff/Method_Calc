import time
import numpy as np
import matplotlib.pyplot as plt
import asyncio

plt.ion()


def f(x):
    return 3 * x - np.exp(x)


def df(x):
    return 3 - np.exp(x)


def ddf(x):
    return -np.exp(x)


def fi(x, L=-0.5):
    return x + L * f(x)


def draw_plots(position_point):
    x_ = np.arange(-10, 10, 1)
    nul_arr = [0] * 20

    x_plt = np.arange(-10, 10, 0.1)
    f_plt = [f(x) for x in x_plt]

    # включение интерактивного режима отображения графиков
    fig, ax = plt.subplots()  # Создание окна и осей для графика
    ax.grid(True)  # отображение сетки на графике

    ax.set(xlim=(-5, 5), ylim=(-5, 5))
    ax.plot(x_plt, f_plt)  # отображение параболы
    ax.plot(x_, nul_arr, c='black')
    ax.plot(nul_arr, x_, c='black')
    point = ax.scatter(position_point[0][0], (position_point[0][1]), c='red')
    for p in position_point:
        point.set_offsets(p)  # отображение точки красным цветом
        # перерисовка графика и задержка на 20 мс
        fig.canvas.draw()
        fig.canvas.flush_events()
        time.sleep(0.4)
    plt.ioff()
    plt.show()


def bisection_1(a, b, eps):
    i = 0
    x_i = (a + b) / 2
    f1, f2 = f(a), f(x_i)
    arr_for_plots = []
    while np.abs(b - a) > eps:
        if f1 * f2 > 0:
            a = x_i
        else:
            b = x_i
        x_i = (a + b) / 2
        f1, f2 = f(a), f(x_i)
        i += 1
        arr_for_plots.append([x_i, f(x_i)])
    draw_plots(arr_for_plots)
    return x_i, f(x_i), i


def fixed_point_iter_2(x, eps):
    i = 0
    while (True):
        y = fi(x)
        c = np.abs(x - y)
        x = y
        i += 1
        if c < eps:
            return x, f(x), i


def Nuton_3(a, eps):
    i = 0
    x = 0
    if f(a) * ddf(a) > 0:
        x = a

    while (True):
        x -= f(x) / df(x)
        i += 1
        if np.abs(f(x)) < eps:
            return x, f(x), i


def Chords_4(a, b, eps):
    i = 0
    if  f(a)*ddf(a)<0:
        print("Начальное условие о сходимости не выполнено")
        return -1
    while (True):
        x = a - f(a) / (f(b) - f(a)) * (b - a)
        if f(x) * f(a):
            a = x
        else:
            b = x
        i += 1
        if np.abs(f(x)) < eps:
            i=3
            return x, f(x), i

def secant(a,b,eps ):
    while np.abs(f(b)>eps):
        a = b - ((b - a) * f(b)) / (f(b) - f(a))
        b = a - ((a - b) * f(a)) / (f(a) - f(b))

        return b

# bisection_1(0.5, 2, 0.001, 0)
#
# fixed_point_iter_2(0.1, 0.0001)
#
# Nuton_3(0,1,0.0001)
#
# Chords_4(0.1, 0.4, 0.0001)
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(bisection_1))
print("Найти приблизительные решения уравнения:\n3 * x - np.exp(x)=0")
while True:
    print('Выберите алгоритм:'
          '\n1)Метод половинного деления'
          '\n2)Метода простых итераций '
          '\n3)Метода касательных (Ньютона) '
          '\n4)Метода хорд')
    choose = int(input())
    if choose == 1:
        print('Введите отрезок а,б')
        a = float(input())
        b = float(input())
        print(f'x\tf(x)\tn\n')
        print(bisection_1(a, b, 0.0001))
    elif choose == 2:
        print('Введите x')
        x = float(input())
        print(f'x\tf(x)\tn\n')
        print(fixed_point_iter_2(x, 0.0001))
    elif choose == 3:
        print('Введите x')
        x = float(input())
        print(f'x\tf(x)\tn\n')
        print(Nuton_3(x, 0.0001))
    elif choose == 4:
        print('Введите неподвижный конец с')
        a = float(input())
        print('Введите подвижный конец x')
        b = float(input())
        print(f'x\tf(x)\tn\n')
        print(Chords_4(a, b, 0.0001))
        # print(secant(a,b,0.0001))
    else:
        break
# print(Nuton_3(0.1, 0.0001))

# print(f'x\tf(x)\tn\n'
#       f'{bisection_1(0.1, 2, 0.0001)}\n'
#       f'{fixed_point_iter_2(0.1, 0.0001)}\n'
#       f'{Nuton_3(0.1, 1, 0.0001)}\n'
#       f'{Chords_4(-2, 0.8, 0.0001)}')
