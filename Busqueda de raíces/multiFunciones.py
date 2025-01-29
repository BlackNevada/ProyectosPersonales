import sys
import numpy as np
import matplotlib.pyplot as plt
from NewtonRaphson import *
from graficador import graficar_funcion

def funcionMultivarLineal(a1, a2, a3, f1, f2, ap1, ap2, ap3, fp1, fp2, t, x):
    g =lambda t, x: a1(t)*f1(x) +a2(t)*f2(x) +a3(t)
    gp=lambda t, x: a1(t)*fp1(x)+a2(t)*fp2(x)
    return g, gp

def buscarEnRango(a1, a2, a3, f1, f2, ap1, ap2, ap3, fp1, fp2, t0, t1, n, x):
    arrx=[]
    x=0
    i=1
    consT=(t1-t0)/n
    while i<=n:
        t=consT*i
        f, fp = funcionMultivarLineal(a1, a2, a3, f1, f2, ap1, ap2, ap3, fp1, fp2, t, x)
        x=buscarRaicesNewtonRaphsonParametrico(f, fp, x, 10, t)
        arrx.append(x)
        i+=1
    return arrx

def defCondiciones():
    a1 =lambda t: -1
    a2 =lambda t: t
    a3 =lambda t: 1+np.exp(-t)

    ap1=lambda t: 0
    ap2=lambda t: 1
    ap3=lambda t: -np.exp(-t)

    f1 =lambda x: x*x
    f2 =lambda x: x
    fp1=lambda x: 2*x
    fp2=lambda x: 1

    t=1
    x=0
    return a1, a2, a3, ap1, ap2, ap3, f1, f2, fp1, fp2, t, x

a1, a2, a3, ap1, ap2, ap3, f1, f2, fp1, fp2, t, x = defCondiciones()

f, fp = funcionMultivarLineal(a1, a2, a3, f1, f2, ap1, ap2, ap3, fp1, fp2, t, x)
x = buscarRaicesNewtonRaphsonParametrico(f, fp, x, 10, t)
print(x)
print(f(t, x))

#graficar_funcion(funcion=f, x_min=-1, x_max=1, num_puntos=100, p=t)

a1, a2, a3, ap1, ap2, ap3, f1, f2, fp1, fp2, t, x = defCondiciones()

arrx=buscarEnRango(a1, a2, a3, f1, f2, ap1, ap2, ap3, fp1, fp2, 1, 11, 10, x)
for i in np.arange(len(arrx)):
    print(f"{i}. ", arrx[i])
