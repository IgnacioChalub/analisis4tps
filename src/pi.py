from math import pi, sqrt
from decimal import Decimal, getcontext
getcontext().prec = 40

def pi_math():
    return pi

def gauss_legendre_float(precision):
    a = 1
    b = 1/sqrt(2)
    t = 1/4
    p = 1
    while(abs(a-b)>precision):
        x = (a+b)/2
        y = sqrt(a*b)
        t = t-p*(a-x)*(a-x)
        a = x
        b = y
        p = 2*p

    return ((a+b)**2)/(4*t)

def gauss_legendre_decimal(precision):
    a = Decimal(1)
    b = Decimal(1)/Decimal.sqrt(Decimal('2'))
    t = Decimal(1)/Decimal('4')
    p = Decimal(1)
    while((Decimal(a)-Decimal(b))>precision):
        x = (Decimal(a)+Decimal(b))/2
        y = sqrt(Decimal(a)*Decimal(b))
        t = Decimal(t)-Decimal(p)(Decimal(a)-Decimal(x))(Decimal(a)-Decimal(x))
        a = x
        b = y
        p = Decimal(2)*Decimal(p)

    return ((Decimal(a)+Decimal(b))**Decimal('2'))/(Decimal('4')*Decimal(t))

def spigot(d):
    x = ""
    q,r,t,k,n,l = 1,0,1,1,3,3
    index = 0
    while len(x) < d+1:
        if index == 2:
            x = x + "."
        index += 1
        if 4*q+r-t < n*t:
            x = x + str(n)
            q,r,t,k,n,l = (
                10*q,10*(r-n*t),t,k,
                (10*(3*q+r))//t-10*n,l)
        else:
            q,r,t,k,n,l = (
                q*k,(2*q+r)*l,t*l,k+1,
                (q*(7*k+2)+r*l)//(t*l),l+2)
    
    return Decimal(x)

pi_math = pi_math()
pi_gauss_legendre_float = gauss_legendre_float(0.000000001)
pi_gauss_legendre_decimal = gauss_legendre_decimal(0.000000001)
pi_spigot = spigot(100)

print("Math: ", pi_math)
print("****")
print("Gauss legendre float: ", pi_gauss_legendre_float)
print("****")
print("Gauss legendre decimal: ", pi_gauss_legendre_decimal)
print("****")
print("Spigot: ", pi_spigot)

print("---------------------------")
print("   ")
print("AREAS (r = 2):")
print("   ")
area_math=  pi_math*2*2
area_gauss_legendre_float = pi_gauss_legendre_float*2*2
area_gauss_legendre_decimal= pi_gauss_legendre_decimal*2*2
area_spigot= pi_spigot*2*2
print("Math: ", pi_math*2*2)
print("****")
print("Gauss legendre float: ", pi_gauss_legendre_float*2*2)
print("****")
print("Gauss legendre decimal: ", pi_gauss_legendre_decimal*2*2)
print("****")
print("Spigot: ", pi_spigot*2*2)
 
print("---------------------------")
print("   ")
print("ERRORES:")
print("   ")
print("Gauss legendre float area error: ", abs(area_math - area_gauss_legendre_float )/area_math)
print("****")
print("Gauss legendre decimal area error: ", abs(Decimal(area_math) - area_gauss_legendre_decimal )/Decimal(area_math))
print("****")
print("Spigot area error: ", abs(Decimal(area_math) - area_spigot)/ Decimal(area_math))
