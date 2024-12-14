import time
import numpy as np
import functools

# Decorador para medir el tiempo de ejecución de una función
def medir_tiempo(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Registrar el tiempo inicial
        result = func(*args, **kwargs)  # Ejecutar la función original
        end_time = time.time()  # Registrar el tiempo final
        execution_time = end_time - start_time
        print(f"El programa '{func.__name__}' tomó {execution_time:.4f} segundos en ejecutarse.")
        return result  # Devolver el resultado de la función original
    return wrapper


@medir_tiempo
def buscarPrimosV0(n):
    i=3
    encontrados=1
    primos=[2]
    while encontrados<n:
        flag=True
        j=0
        while j<len(primos):
            if i/primos[j] == i//primos[j]:
                flag=False
            j+=1
        if flag:
            encontrados+=1
            primos.append(i)
            print(encontrados, i)
        i+=1
    return primos[-1]

@medir_tiempo
def buscarPrimosV1(n):
    i=3
    encontrados=1
    primos=[2]
    while encontrados<n:
        flag=True
        j=0
        posibles=len(primos)
        while flag and j<posibles//primos[j]:
            if i/primos[j] == i//primos[j]:
                flag=False
            j+=1
        if flag:
            encontrados+=1
            primos.append(i)
            print(encontrados, i)
        i+=2
    return primos[-1]

@medir_tiempo
def buscarPrimosV2(n):
    if n==1:
        return 2, 1
    i=5
    encontrados=2
    primos=np.array([3])
    potprims=np.array([9])
    while encontrados<n:
        for primo, pp in zip(primos, potprims):
            if pp>i:
                encontrados+=1
                primos=np.append(primos, i)
                potprims=np.append(potprims, i*i)
                if i%2621==1:
                    print(encontrados, i)
                break
            if i%primo==0:
                break
        i+=2
    return primos[-1]
    
@medir_tiempo
def buscarPrimos(n):
    if n==1:
        return 2, 1
    i=5
    encontrados=2
    primos=np.array([3])
    potprims=np.array([9])
    while encontrados<n:
        for primo in primos:
            if primo*primo>i:
                encontrados+=1
                primos=np.append(primos, i)
                if i%12621==1:
                    print(encontrados, i)
                break
            if i%primo==0:
                break
        i+=2
    return primos[-1]
    
print("Elija qué función ocupar: ")
i=0
for func in [buscarPrimosV0, buscarPrimosV1, buscarPrimos]:
    print(f"Elija {i} para la función: {func.__name__}")
    i+=1

opt=int(input())
n=input("Elija el n-ésimo primo que quiere encontrar.\nElija un número: ")
match opt:
    case 0:
        r = buscarPrimosV0(int(n))
    case 1:
        r = buscarPrimosV1(int(n))
    case 2:
        r = buscarPrimos(int(n))

print(r)
