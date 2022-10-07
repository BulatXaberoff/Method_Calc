import sympy

def Eiler(a,b,h,n,x0,y0,z0,func1,func2):
    x_i,y_i,z_i=x0,y0,z0
    i=0
    while(x_i<b):
        i += 1
        y_i += float(h * func1.subs([(x,x_i),(y,y_i),(z,z_i)]))
        z_i += float(h * func2.subs([(x,x_i),(y,y_i),(z,z_i)]))
        x_i += i * h

    return x_i,y_i,z_i
def Runge_Cutta(a,b,x0,y0,z0,h,n,func1,func2):
  k1 = float(func1.subs([(x,x0),(y,y0),(z,z0)]))*h
  l1 = float(func1.subs([(x,x0),(y,y0),(z,z0)]))*h
  
  k2 = float(func1.subs([(x,x0 + h/2) ,(y,y0 + k1/2),(z,z0 + l1/2)]))*h
  l2 = float(func2.subs([(x,x0 + h/2) ,(y,y0 + k1/2),(z,z0 + l1/2)]))*h
  
  k3 = float(func1.subs([(x,x0 + h/2), (y,y0 + k2/2),(z,z0 + l2/2)]))*h
  l3 = float(func2.subs([(x,x0 + h/2), (y,y0 + k2/2),(z,z0 + l2/1)]))*h
  
  k4 = float(func1.subs([(x,x0 + h), (y,y0 + k3),(z,z0 + l3)]))*h
  l4 = float(func2.subs([(x,x0 + h), (y,y0 + k3),(z,z0 + l3)]))*h
  
  delta_y0 = h/6 * (k1 + 2*k2 + 2*k3 + k4)
  y_i = y0 + delta_y0

  delta_z0 = h/6 * (l1 + 2*l2 + 2*l3 + l4)
  z_i = z0 + delta_z0
  for i in range(1,n):
    # print(y_i)
    # print(delta_y0)
    x_i = i * h
    k1 = float(func1.subs([(x,x0 + x_i),(y,y_i),(z,z_i)]))*h
    l1 = float(func1.subs([(x,x0 + x_i),(y,y_i),(z,z_i)]))*h
    
    k2 = float(func1.subs([(x,x0 + h/2 + x_i) ,(y,y_i + k1/2),(z,z_i + l1/2)]))*h
    l2 = float(func2.subs([(x,x0 + h/2 + x_i) ,(y,y_i + k1/2),(z,z_i + l1/2)]))*h
    
    k3 = float(func1.subs([(x,x0 + h/2 + x_i), (y,y_i + k2/2),(z,z_i + l2/2)]))*h
    l3 = float(func2.subs([(x,x0 + h/2 + x_i), (y,y_i + k2/2),(z,z_i + l2/1)]))*h
    
    k4 = float(func1.subs([(x,x0 + h + x_i), (y,y_i + k3),(z,z_i + l3)]))*h
    l4 = float(func2.subs([(x,x0 + h + x_i), (y,y_i + k3),(z,z_i + l3)]))*h
    
    delta_y0 = h/6 * (k1 + 2*k2 + 2*k3 + k4)
    y_i = y_i + delta_y0

    delta_z0 = h/6 * (l1 + 2*l2 + 2*l3 + l4)
    z_i = z_i + delta_z0

  return x_i,y_i,z_i



x=sympy.symbols('x')
y=sympy.symbols('y')
z=sympy.symbols('z')

dy_dx=z
dz_dx=-0.1*z-3.2*y
x0=0
y0=1
z0=0
a,b=0,1
h=0.1

print(Eiler(a,b,h,10,x0,y0,z0,dy_dx,dz_dx))
print(Runge_Cutta(a,b,x0,y0,z0,h,10,dy_dx,dz_dx))
