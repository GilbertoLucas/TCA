import time
import numpy
from Order import *
import matplotlib.pyplot as plt


# Tamanho dos vetores
n = [10, 100, 1000]

# Vetor para armazenar os tempos
time_selection = []
time_mergesort = []
time_quicksort = []
time_insertion = []

for i in range(len(n)):
    #lista de numeros aleatorios
    random_numbers = numpy.random.uniform(size=n[i]).tolist()

    #Lista em ordem crescente
    random_numbers_crescente = sorted(random_numbers)

    #Lista em ordem decrescente
    random_numbers_decrescente = sorted(random_numbers, reverse=True)

    list_random_numbers = [random_numbers, random_numbers_crescente, random_numbers_decrescente]

    for j in range(len(list_random_numbers)):
        #selection
        OrderedList = ['' for i in range(len(list_random_numbers[j]))]
        t0_selection_random = time.time()
        OrderedList_selection = selection(list_random_numbers[j], OrderedList)
        tf_selection_random = time.time()

        time_selection_random = "{:.20f}".format(tf_selection_random - t0_selection_random)
        time_selection.append(float(time_selection_random))

        # mergesort
        t0_mergesort_random = time.time()
        OrderedList_mergesort = mergesort(list_random_numbers[j])
        tf_mergesort_random = time.time()

        time_mergesort_random = "{:.20f}".format(tf_mergesort_random - t0_mergesort_random)
        time_mergesort.append(float(time_mergesort_random))

        # quicksort
        OrderedList = ['' for i in range(len(list_random_numbers[j]))]
        t0_quicksort_random = time.time()
        OrderedList_quicksort = QuickSort(list_random_numbers[j], OrderedList)
        tf_quicksort_random = time.time()

        time_quicksort_random = "{:.20f}".format(tf_quicksort_random - t0_quicksort_random)
        time_quicksort.append(float(time_quicksort_random))

        # insertion
        t0_insertion_random = time.time()
        OrderedList_insertion = insertion(list_random_numbers[j])
        tf_insertion_random = time.time()

        time_insertion_random = "{:.20f}".format(tf_insertion_random - t0_insertion_random)
        time_insertion.append(float(time_insertion_random))

# organizando os dados
random_selection = []
crescent_selection = []
decrescente_selection = []

random_mergesort = []
crescent_mergesort = []
decrescente_mergesort = []

random_quicksort = []
crescent_quicksort = []
decrescente_quicksort = []

random_inserction = []
crescent_inserction = []
decrescente_inserction = []

for k in range(len(n)):
    random_selection.append(time_selection[3*k])
    crescent_selection.append(time_selection[3*k+1])
    decrescente_selection.append(time_selection[3*k+2])

    random_quicksort.append(time_quicksort[3*k])
    crescent_quicksort.append(time_quicksort[3*k+1])
    decrescente_quicksort.append(time_quicksort[3*k+2])

    random_mergesort.append(time_mergesort[3*k])
    crescent_mergesort.append(time_mergesort[3*k+1])
    decrescente_mergesort.append(time_mergesort[3*k+2])

    random_inserction.append(time_insertion[3*k])
    crescent_inserction.append(time_insertion[3*k+1])
    decrescente_inserction.append(time_insertion[3*k+2])


# plotando resultados random
plt.title("Valores aleatórios")
plt.plot(n, random_selection, '-d', label="Seleção")
plt.plot(n, random_mergesort, '-d', label="Mergesort")
plt.plot(n, random_quicksort, '-d', label="Quicksort")
plt.plot(n, random_inserction, '-d', label="Inserção")
plt.xlabel("Número de valores")
plt.ylabel("Tempo (segundos)")
plt.legend()
plt.grid()
plt.show()
plt.savefig("result_random" + ".pdf")

# plotando resultados crescentes
plt.title("Valores em ordem crescente")
plt.plot(n, crescent_selection, '-d', label="Seleção")
plt.plot(n, crescent_mergesort,'-d', label="Mergesort")
plt.plot(n, crescent_quicksort, '-d', label="Quicksort")
plt.plot(n, crescent_inserction,'-d', label="Inserção")
plt.xlabel("Número de valores")
plt.ylabel("Tempo (segundos)")
plt.legend()
plt.grid()
plt.show()
plt.savefig("result_crescent" + ".pdf")

# plotando resultados decrescente
plt.title("Valores em ordem decrescente")
plt.plot(n, decrescente_selection, '-d', label="Seleção")
plt.plot(n, decrescente_mergesort,'-d', label="Mergesort")
plt.plot(n, decrescente_quicksort, '-d', label="Quicksort")
plt.plot(n, decrescente_inserction,'-d', label="Inserção")
plt.xlabel("Número de valores")
plt.ylabel("Tempo (segundos)")
plt.legend()
plt.grid()
plt.show()
plt.savefig("result_decrescente" + ".pdf")