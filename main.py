from sort import ordenamientoBurbuja
from sort import ordenamientoPorInsercion
from generador import genera_aleatorio
from generador import genera_ordenado
from generador import genera_invertido
from time import time

aux = [1000,10000]
for i in range(100000,1100000,100000):
    aux.append(i)

#BubbleSort Ordenado
tiempo_ordenado_bubble = []
for i in aux:
    ordenado = genera_ordenado(i)
    tiempo_inicial = time()
    ordenamientoBurbuja(ordenado)
    tiempo_final = time()
    tiempo_ejecucion = tiempo_final - tiempo_inicial
    tiempo_ordenado_bubble.append(tiempo_ejecucion)
    print("TERMINE UNA ITERACIÓN")

"""
#BubbleSort Invertido
tiempo_invertido_bubble = []
for i in aux:
    ordenado = genera_invertido(i)
    tiempo_inicial = time()
    ordenamientoBurbuja(ordenado)
    tiempo_final = time()
    tiempo_ejecucion = tiempo_final - tiempo_inicial
    tiempo_ordenado_bubble.append(tiempo_ejecucion)

#BubbleSort Aleatorio
tiempo_aleatorio_bubble = []
for i in aux:
    ordenado = genera_aleatorio(i)
    tiempo_inicial = time()
    ordenamientoBurbuja(ordenado)
    tiempo_final = time()
    tiempo_ejecucion = tiempo_final - tiempo_inicial
    tiempo_ordenado_bubble.append(tiempo_ejecucion)
"""
