import sys
import numpy as np
import matplotlib.pyplot as plt
from NewtonRaphson import *
from graficador import graficar_funcion

def data_transmission(tk, Delta_k, rho, xt, yt, xpt, ypt, px, py):
    f =lambda t: (np.power((xt(t)-px), 2)+np.power((yt(t)-py), 2)-rho*rho)
    fp=lambda t: 4*((xt(t)-px)*xpt(t)+(yt(t)-py)*ypt(t)-rho*rho)
    t1=tk+Delta_k
    
    a0=buscarRaicesNewtonRaphson(f, fp, t1, 10)
    a1=buscarRaicesNewtonRaphson(f, fp, t1, 11)
    a2=buscarRaicesNewtonRaphson(f, fp, t1, 12)
    
    #print(a0, a1, a2)
    s=np.abs((a2-a1)/(a1-a0))
    m=1/(1-s)
    f =lambda t: m*(np.power((xt(t)-px), 2)+np.power((yt(t)-py), 2)-rho*rho)
    t1=buscarRaicesNewtonRaphson(f, fp, t1, 10)
    
    f =lambda t: np.sqrt(np.power((xt(t)-px), 2) +np.power((yt(t)-py), 2))-rho
    if f((tk+t1)/2)>0:
        transmission = False
    else:
        transmission = True
        
    return t1, transmission
    
xt =lambda t: np.sin(t)+1
yt =lambda t: 0
xpt=lambda t: np.cos(t)
ypt=lambda t: 0

tk=3.1415926536*2
Delta_k=3.1415926536
rho=1
px, py=0, 0

t1, transmission=data_transmission(tk, Delta_k, rho, xt, yt, xpt, ypt, px, py)
print("t1:   ", t1)

f =lambda t: np.power((np.power((xt(t)-px), 2) +np.power((yt(t)-py), 2) -rho*rho), 2)

print("f(t1):", f(t1))

print("transmission?: ", transmission)

f =lambda t: np.power(np.power((xt(t)-px), 2) +np.power((yt(t)-py), 2), 0.5)-rho
graficar_funcion(f, 0, 10, num_puntos=100, p=0)

#f =lambda t: np.power((np.power((xt(t)-px), 2) +np.power((yt(t)-py), 2) -rho*rho), 2)
#graficar_funcion(f, 0, 7, num_puntos=100, p=0)
