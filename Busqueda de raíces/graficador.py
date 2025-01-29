import sys
import numpy as np
import matplotlib.pyplot as plt

def graficar_funcion(funcion, x_min, x_max, num_puntos=100, p=0):
    x = np.linspace(x_min, x_max, num_puntos)
    if p:
        y = funcion(p, x)
    else:
        y = funcion(x)
    
    plt.plot(x, y, label=f'{funcion.__name__}(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Gráfico de {funcion.__name__}(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

    puntos = np.column_stack((x, y))
    np.savetxt(f'{funcion.__name__}_puntos.csv', puntos, delimiter=',', header='x,y', comments='')
