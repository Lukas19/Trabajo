#BubbleSort
def ordenamientoBurbuja(unaLista):
    for numPasada in range(len(unaLista)-1,0,-1):
        for i in range(numPasada):
            if unaLista[i]>unaLista[i+1]:
                temp = unaLista[i] 
                unaLista[i] = unaLista[i+1] 
                unaLista[i+1] = temp
    return unaLista

#Insertion Sort
def ordenamientoPorInsercion(unaLista): 
    for indice in range(1,len(unaLista)):
        valorActual = unaLista[indice]
        posicion = indice
        while posicion>0 and unaLista[posicion-1]>valorActual:
            unaLista[posicion]=unaLista[posicion-1]
            posicion = posicion-1 
        unaLista[posicion]=valorActual
    return unaLista

#Quick Sort
def ordenamientoRapido(unaLista): 
    ordenamientoRapidoAuxiliar(unaLista,0,len(unaLista)-1)

def ordenamientoRapidoAuxiliar(unaLista,primero,ultimo): 
    if primero<ultimo:
        puntoDivision = particion(unaLista,primero,ultimo) 
        ordenamientoRapidoAuxiliar(unaLista,primero,puntoDivision-1) 
        ordenamientoRapidoAuxiliar(unaLista,puntoDivision+1,ultimo)

def particion(unaLista,primero,ultimo): 
    valorPivote = unaLista[primero] 
    marcaIzq = primero+1
    marcaDer = ultimo
    hecho = False 
    while not hecho:
        while marcaIzq <= marcaDer and unaLista[marcaIzq] <= valorPivote: 
            marcaIzq = marcaIzq + 1
        while unaLista[marcaDer] >= valorPivote and marcaDer >= marcaIzq: 
            marcaDer = marcaDer -1
        if marcaDer < marcaIzq: 
            hecho = True
        else:
            temp = unaLista[marcaIzq] 
            unaLista[marcaIzq] = unaLista[marcaDer] 
            unaLista[marcaDer] = temp
    temp = unaLista[primero] 
    unaLista[primero] = unaLista[marcaDer] 
    unaLista[marcaDer] = temp
    return marcaDer