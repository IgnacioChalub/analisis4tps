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


def f(x, y):
    return 

print('Euler normal: ')
array = euler_mejorado(f, 0, 2, 0.5, 2)
print(array)