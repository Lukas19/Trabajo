from random import randint 
import numpy as np

def genera_aleatorio(n):
    aux = []
    for i in range(n):
        aux.append(i)
    return np.array(aux)

def genera_ordenado(n):
    aux = []
    for i in range(n):
        aux.append(i)
    return np.array(aux)

def genera_invertido(n): 
    i=n
    aux = []
    while (i > 0):
        aux.append(i)
        i=i-1
    return np.array(aux)
