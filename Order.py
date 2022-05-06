def selection(lista, OrderedLists):
    if len(lista) == 0:
        return OrderedLists  # lista vazia

    x = lista
    N = len(x)
    for i in range(N - 1):
        id_menor = i  # menor elemento e' o elemento[i]
        for j in range(i + 1, N):  # varredura nos elementos apos  i
            if (x[j] < x[id_menor]):  # caso encontrar um elemento[j] com valor menor do que elemento[i]
                id_menor = j  # menor valor atualizado para elemento [j]
        x[i], x[id_menor] = x[id_menor], x[i]  # troca de posicao do i com o novo menor elemento

    OrderedLists = x
    return OrderedLists


def QuickSort(lists, OrderedLists, index=0):
    if len(lists) == 0:
        return OrderedLists  # lista vazia

    pivot = lists[int(len(lists) / 2)]  # Escolhendo como pivo o elemento central do vetor
    lists.remove(pivot)  # removendo o pivo da lista

    right_values = []
    left_values = []

    # Separacao
    for i in lists:
        if i > pivot:
            right_values.append(i)  # valores maiores que o pivo vao para o subvetor direito
        else:
            left_values.append(i)  # valores menores ou iguais que o pivo vao para o subvetor esquerdo

    OrderedLists[index + len(left_values)] = pivot  # posicionamento do pivo no vetor com valores ordenados

    # recursao
    QuickSort(right_values, OrderedLists, index + len(left_values) + 1)  # recursao do lado direito
    QuickSort(left_values, OrderedLists, index)  # recursao do lado esquerdo

    return OrderedLists


def mergesort(x):
    n = len(x)
    if n < 2:  # caso básico da recursão
        return x

    m = n // 2
    l = x[0:m]  # separação
    r = x[m:n]

    mergesort(l)  # recursão
    mergesort(r)

    i = 0
    j = 0

    for k in range(n):  # combinação
        if l[i] < r[j]:
            x[k] = l[i]
            i = i + 1
        else:
            x[k] = r[j]
            j = j + 1

        if j >= len(r):
            r.append(float('inf'))  # adicionando as sentinelas
        if i >= len(l):
            l.append(float('inf'))

    return x


def insertion(x):
    n = len(x)

    for i in range(1, n):
        v = x[i]
        j = i

        while j - 1 >= 0 and x[j - 1] > v:
            x[j] = x[j - 1]
            j = j - 1

        x[j] = v

    return x


# from wikipedia

# def mergeSort(lista):
#     if len(lista) > 1:
#
#         meio = len(lista) // 2
#         # também é valido: meio = int(len(lista)/2)
#
#         listaDaEsquerda = lista[:meio]
#         listaDaDireita = lista[meio:]
#
#         mergeSort(listaDaEsquerda)
#         mergeSort(listaDaDireita)
#
#         i = 0
#         j = 0
#         k = 0
#
#         while i < len(listaDaEsquerda) and j < len(listaDaDireita):
#
#             if listaDaEsquerda[i] < listaDaDireita[j]:
#                 lista[k] = listaDaEsquerda[i]
#                 i += 1
#             else:
#                 lista[k] = listaDaDireita[j]
#                 j += 1
#             k += 1
#
#         while i < len(listaDaEsquerda):
#             lista[k] = listaDaEsquerda[i]
#             i += 1
#             k += 1
#
#         while j < len(listaDaDireita):
#             lista[k] = listaDaDireita[j]
#             j += 1
#             k += 1
#     return lista

# def partition(array, start, end):
#     pivot = array[start]
#     low = start + 1
#     high = end
#
#     while True:
#         # If the current value we're looking at is larger than the pivot
#         # it's in the right place (right side of pivot) and we can move left,
#         # to the next element.
#         # We also need to make sure we haven't surpassed the low pointer, since that
#         # indicates we have already moved all the elements to their correct side of the pivot
#         while low <= high and array[high] >= pivot:
#             high = high - 1
#
#         # Opposite process of the one above
#         while low <= high and array[low] <= pivot:
#             low = low + 1
#
#         # We either found a value for both high and low that is out of order
#         # or low is higher than high, in which case we exit the loop
#         if low <= high:
#             array[low], array[high] = array[high], array[low]
#             # The loop continues
#         else:
#             # We exit out of the loop
#             break
#
#     array[start], array[high] = array[high], array[start]
#
#     return high
#
# def quick_sort(array, start, end):
#     if start >= end:
#         return
#
#     p = partition(array, start, end)
#     quick_sort(array, start, p-1)
#     quick_sort(array, p+1, end)

# def QuickSort(arr):
#     elements = len(arr)
#
#     # Base case
#     if elements < 2:
#         return arr
#
#     current_position = 0  # Position of the partitioning element
#
#     for i in range(1, elements):  # Partitioning loop
#         if arr[i] <= arr[0]:
#             current_position += 1
#             temp = arr[i]
#             arr[i] = arr[current_position]
#             arr[current_position] = temp
#
#     temp = arr[0]
#     arr[0] = arr[current_position]
#     arr[current_position] = temp  # Brings pivot to it's appropriate position
#
#     left = QuickSort(arr[0:current_position])  # Sorts the elements to the left of pivot
#     right = QuickSort(arr[current_position + 1:elements])  # sorts the elements to the right of pivot
#
#     arr = left + [arr[current_position]] + right  # Merging everything together
#
#     return arr


# def quicksort(x, r=0, s=None):
#     s = s if s is not None else len(x) - 1
#     if r < s:
#
#         v = x[r]
#         i = r
#         j = s
#
#         while i <= j:
#             while (x[i] < v):
#                 i += 1
#             while (x[j] > v):
#                 j += -1
#             if (i <= j):
#                 aux = x[i]
#                 x[i] = x[j]
#                 x[j] = aux
#                 i += 1
#                 j += -1
#
#         quicksort(x, r, j)
#         quicksort(x, i, s)
#
#     return x
