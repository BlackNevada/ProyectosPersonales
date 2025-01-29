import sys
import numpy as np
import matplotlib.pyplot as plt

def buscarRaicesNewtonRaphson(f, fp, x, m):
    g=lambda x: x-f(x)/fp(x)
    i=0
    while i<m:
    	x=g(x)
    	i+=1
    return x



def buscarRaicesNewtonRaphsonParametrico(f, fp, x, m, p):
    g=lambda x: x-f(p, x)/fp(p, x)
    i=0
    while i<m:
    	x=g(x)
    	i+=1
    return x
