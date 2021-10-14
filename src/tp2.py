import math

def euler(f, x0, y0, h, n):
    array = [[0]*n, [0]*n]
    for i in range(n):
        y1 = y0 + h*f(x0, y0)
        x0 = x0 + h
        y0 = y1
        array[0][i] = x0
        array[1][i] = y0
    return array

def euler_mejorado(f, x0, y0, h, n):
    array = [[0]*n, [0]*n]
    for i in range(n):
        k1 = h * f(x0, y0)
        k2 = h * f(x0+h, y0 + k1)
        y1 = y0 + 0.5 * (k1 + k2)

        x0 = x0 + h
        y0 = y1
        array[0][i] = x0
        array[1][i] = y0
    return array

def euler_modificado(f, x0, y0, h, n):
    array = [[0]*n, [0]*n]
    for i in range(n):
        k1 = h * f(x0, y0)
        k2 = h * f(x0+0.5*h, y0 + 0.5 * k1)
        y1 = y0 + k2

        x0 = x0 + h
        y0 = y1
        array[0][i] = x0
        array[1][i] = y0
    return array

def runge_kutta_4to(f, x0, y0, h, n):
    array = [[0]*n, [0]*n]
    for i in range(n):
        k1 = h * f(x0, y0)
        k2 = h * f(x0+0.5*h, y0 + 0.5 * k1)
        k3 = h * f(x0+0.5*h, y0*0.5*k2)
        k4 = h * f(x0+0.5, y0+ k3)

        y1 = y0 + (1/6) * (k1 + 2*k2 + 2*k3 + k4)

        x0 = x0 + h
        y0 = y1
        array[0][i] = x0
        array[1][i] = y0
    return array

def k(x, y, z, w):
    return math.exp(x) - 2*g(x,y,z,w) + f(x,y,z,w) + 2*y

def g(x, y, z, w):
    return w

def f(x,y,z,w):
    return z

print('Euler normal: ')
array = runge_kutta_4to(k, 0, -1, 0.5, 2)
print(array)