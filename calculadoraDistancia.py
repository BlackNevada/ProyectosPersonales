import numpy as np

def pitagoras():
 x=int(input("Distancia x: "))
 y=int(input("Distancia y: "))
 r=np.round(np.sqrt(x*x+y*y), 2)
 return r



print("Elija el modo:")
print("1-. Config rápida")
print("2-. Cálculo completo")
#print("3-. Cálcular salto")

modo=int(input())

r=0
if modo==2:
 mov=int(input("Movimiento: "))
 adjmov=mov+2.5
 inside=False
 r+=int(input("Distancia inicial: "))

r+=pitagoras()
print("Total Distance:", r)

if modo==2:
 if r<=adjmov:
  inside=True
 print("Base movement:", mov)
 print("Adjusted movement:", adjmov)
 print("Inside:", inside)
 
 
'''
if modo==3:
 print("Ingrese tipo de salto:")
 print("1-. Largo        2-. Alto")
 tipoSalto=int(input())
 strength=int(input("Strength score: "))
 if tipoSalto==1:
  x=strength/2
  y=x-x**2/strength
  print("Altura máxima:")
 if tiposalto==2:
  
 #y=x-x**2/strength
 #v0=1/(4.9*strength)
'''
