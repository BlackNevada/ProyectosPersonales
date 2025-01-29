import sys
import numpy as np
import matplotlib.pyplot as plt
from NewtonRaphson import *
from graficador import graficar_funcion

#def calcular convergencia()

f1= lambda x, y: x-1+y*np.sin(np.log(y*y+1)-y)
fp1= lambda x, y: np.sin(np.log(y*y+1)-y) + y*np.cos(np.log(y*y+1)-y)*(2*y/(y*y+1)-1)
a=sys.argv
#print(f1(int(a[1]), int(a[2])))
#print(fp1(int(a[1]), int(a[2])))
x=buscarRaicesNewtonRaphsonParametrico(f1, fp1, int(a[1]), int(a[2]), int(a[3]))
print(x)
print(f1(int(a[3]), x))

graficar_funcion(funcion=f1, x_min=-6, x_max=-5, num_puntos=100, p=int(a[3]))
