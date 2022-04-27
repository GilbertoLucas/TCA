def selection(lista):
    x = lista
    N = len(x)
    for i in range(N-1):
        id_menor = i
        for j in range(i+1,N):
            if(x[j] < x[id_menor]):
                id_menor = j
        x[i],x[id_menor] = x[id_menor],x[i]
    
def partition(lista,inicio,fim):
    pivo = lista[fim]
    i = inicio
    for j in range(inicio,fim):
        if lista[j] <= pivo:
            lista[j],lista[i] = lista[i],lista[j]
            i = i + 1
    lista[i], lista[fim] = lista[fim], lista[i]
    return i 
    
    
def quicksort(lista, inicio = 0,fim = None):

    if fim is None:
        fim = len(lista) - 1
    if inicio < fim:
        p = partition(lista,inicio,fim)
        quicksort(lista,inicio,p-1)
        quicksort(lista,p+1,fim)