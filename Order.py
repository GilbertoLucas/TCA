def selection(lista, OrderedLists):
    if len(lista)==0:
        return OrderedLists                      # lista vazia 
    
    x = lista
    N = len(x)
    for i in range(N-1):
        id_menor = i                             # menor elemento e' o elemento[i]
        for j in range(i+1,N):                   # varredura nos elementos apos  i
            if(x[j] < x[id_menor]):              # caso encontrar um elemento[j] com valor menor do que elemento[i]
                id_menor = j                     # menor valor atualizado para elemento [j]
        x[i],x[id_menor] = x[id_menor],x[i]      # troca de posicao do i com o novo menor elemento


    OrderedLists = x
    return OrderedLists
    
    
def QuickSort(lists, OrderedLists,index=0):

    if len(lists)==0:
        return OrderedLists                     # lista vazia 
    
    pivot =  lists[int(len(lists)/2)]           # Escolhendo como pivo o elemento central do vetor
    lists.remove(pivot)                         # removendo o pivo da lista
    
    right_values = []; left_values =[]

    #Separacao
    for i in lists:
        if i>pivot:
            right_values.append(i)              # valores maiores que o pivo vao para o subvetor direito
        else:
            left_values.append(i)               # valores menores ou iguais que o pivo vao para o subvetor esquerdo
    
    OrderedLists[index+len(left_values)]= pivot # posicionamento do pivo no vetor com valores ordenados
    
    #recursao
    QuickSort(right_values, OrderedLists, index+len(left_values)+1)     # recursao do lado direito
    QuickSort(left_values,OrderedLists,index)                           # recursao do lado esquerdo
    
    return OrderedLists


def mergesort(x):

    n = len(x)
    if n < 2:                   # caso básico da recursão
        return x

    m = n // 2
    l = x[0:m]                  # separação
    r = x[m:n]

    mergesort(l)                # recursão
    mergesort(r)

    i = 0
    j = 0

    for k in range(n):          # combinação
        if l[i] < r[j]:
            x[k] = l[i]
            i = i + 1
        else:
            x[k] = r[j]
            j = j + 1

        l.append(float('inf'))  # adicionando as sentinelas
        r.append(float('inf'))

    return x


def insertion(x):

    n = len(x)

    for i in range(1, n):
        v = x[i]
        j = i

        while j-1 >= 0 and x[j-1] > v:
            x[j] = x[j-1]
            j = j - 1

        x[j] = v

    return x