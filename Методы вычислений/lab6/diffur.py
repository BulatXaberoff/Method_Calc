from cProfile import label
import sympy
import matplotlib.pyplot as plt
import numpy as np
import json
import pandas as pd

def method_eiler(x0,y0,h,func):
  n=10
  arr_x=[]
  arr_y=[]
  x_i , y_i = x0,y0
  arr_x.append(x0)
  arr_y.append(y0)
  res = func.subs([(x, x_i), (y, y_i)])
  for i in range(1,n+1):
    x_i , y_i =  i * h + x0 , y_i + h * res
    res = float(func.subs([(x, x_i), (y, y_i)]))
    arr_x.append(x_i)
    arr_y.append(y_i)
  return arr_x,arr_y,float(y_i)

def Runge_Cutta(a,b,x0,y0,h,n,func):
  arrx=[]
  arry=[]
  arrx.append(x0)
  k1 = float(func.subs([(x,x0),[y,y0]]))
  k2 = float(func.subs([(x,x0 + h/2) ,(y,y0 + h/2 * k1)]))
  k3 = float(func.subs([(x,x0 + h/2), (y,y0 + h/2 * k2)]))
  k4 = float(func.subs([(x,x0 + h), (y,y0 + h * k3)]))
  delta_y0 = h/6 * (k1 + 2*k2 + 2*k3 + k4)
  y_i = y0 + delta_y0
  arry.append(y_i)
  for i in range(1,n):
    # print(y_i)
    # print(delta_y0)
    arrx.append(x0 + i*h)
    k1 = float(func.subs([(x,x0 + i*h),(y,y_i)]))
    k2 = float(func.subs([(x,x0 + h/2 + i*h) ,(y,y_i + h/2 * k1)]))
    k3 = float(func.subs([(x,x0 + h/2 + i*h), (y,y_i + h/2 * k2)]))
    k4 = float(func.subs([(x,x0 + h + i*h), (y,y_i + h * k3)]))
    delta_y0 = h/6 * (k1 + 2*k2 + 2*k3 + k4)
    y_i = y_i + delta_y0
    arry.append(y_i)
    
  return arrx,arry,float(y_i)
def plot_s(x,y,x1,y1,x2,y2):
  plt.subplot(1,2,1)
  plt.suptitle("1)Метод Эйлера 2)Метод Рунге-Кутта")
  plt.plot(x,y,linewidth=2.0,label="Исходная функция")
  plt.plot(x1,y1,linewidth=2.0, label="Приближенные значения функции")
  plt.legend()
  plt.subplot(1,2,2)
  plt.plot(x,y,linewidth=2.0,label="Исходная функция")
  plt.plot(x2,y2,linewidth=2.0,label="Приближенные значения функции")
  plt.legend()
  plt.show()


x = sympy.Symbol('x')
y = sympy.Symbol('y')
# df = x + y
# x0=0
# y0=1
# h=0.1
# a=2.1
# b=3.1
df = -2*y + x*x
f = 3/4*sympy.exp(-2*x)+1/2*x*x-1/2*x+1/4
arr_X=np.arange(0,1,0.1)
arr_Y=[f.subs({x:arr_X[i]})for i in range(0,len(arr_X))]

x0=0
y0=1
a,b=0,1
h=0.1
x_1,y_1,res = method_eiler(x0,y0,h,df)
x_2,y_2,res = Runge_Cutta(a,b,x0,y0,h,10,df)
plot_s(arr_X,arr_Y,x_1,y_1,x_2,y_2)

# print(f"Метод Эйлера\nx:{x_1}\t\t\t\t\t\t\ty:{y_1}")
# print(f"Метод Рунге-Кутта\nx:{x_2}\t\t\t\t\t\t\ty:{y_2}")
# np.savetxt("Метод эйлера.txt",(x_1,y_1))
# np.savetxt("Метод Рунге-Кутта.txt",(x_2,y_2))
M_E=pd.DataFrame(list(zip(x_1,y_1)),columns=['X','Y'])
print("Метод Эйлера")
print(M_E)
print("Метод Рунге-Кутта")
M_RG = pd.DataFrame(list(zip(x_2,y_2)),columns=['X','Y'])
print(M_RG)
