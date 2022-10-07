import sympy
 
def sympson(left, right, n, function):
    h = (right - left) / (n)
 
    tmp_sum = float(function.subs({x: left})) +\
        float(function.subs({x: right}))
 
    for step in range(1,n):
        if step % 2 != 0:
            tmp_sum += 4 * float(function.subs({x: left + step * h}))
        else:
            tmp_sum += 2 * float(function.subs({x: left + step * h}))
 
    return tmp_sum * h / 3
 
def trapet(left, right, n, function):
  h = (right - left) / n
  tmp_sum = float(function.subs({x: left})) +\
        float(function.subs({x: right}))/2
  for step in range(1,n-1):
    tmp_sum += function.subs({x:left + step * h})
  return tmp_sum*h

def rectangle_left(a,b,n,func):
    h=(b-a)/n
    res=sum([func.subs({x:(a+(i*h))})for i in range(0,n)])
    res*=h
    return res
def rectangle_right(a,b,n,func):
    h=(b-a)/n
    res=sum([func.subs({x:(a+(i*h))})for i in range(1,n)])
    res*=h
    return res
def rectangle_average(a,b,n,func):
    h=(b-a)/n
    res=sum([func.subs({x:(a + h*i+h/2)})for i in range(0,n)])
    res*=h
    return res

x = sympy.Symbol('x')
a=0.6
b=1.4
n=50
f_x = 1/(12*x**2+0.5)**(1/2)
print(f"Метод Симпсона\t{sympson(a, b, n, f_x)}")
print(f"Метод Трапеции {trapet(a,b,n,f_x)}")
print(f"Метод левых прямоугольников {rectangle_left(a,b,n,f_x)}")
print(f"Метод правых прямоугольников {rectangle_right(a,b,n,f_x)}")
print(f"Метод средних прямоугольников {rectangle_average(a,b,n,f_x)}")