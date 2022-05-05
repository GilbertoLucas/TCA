import time
import numpy
from Order import *
import matplotlib.pyplot as plt
import copy


# Tamanho dos vetores
n = [10, 100, 1000, 10000]#, 100000]

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

    list_random_numbers_selection = [copy.deepcopy(random_numbers), copy.deepcopy(random_numbers_crescente), copy.deepcopy(random_numbers_decrescente)]
    list_random_numbers_quicksort = [copy.deepcopy(random_numbers), copy.deepcopy(random_numbers_crescente), copy.deepcopy(random_numbers_decrescente)]
    list_random_numbers_mergesort = [copy.deepcopy(random_numbers), copy.deepcopy(random_numbers_crescente), copy.deepcopy(random_numbers_decrescente)]
    list_random_numbers_insertion = [copy.deepcopy(random_numbers), copy.deepcopy(random_numbers_crescente), copy.deepcopy(random_numbers_decrescente)]

    for j in range(len(list_random_numbers_selection)):
        #selection
        OrderedList = ['' for i in range(len(list_random_numbers_selection[j]))]
        t0_selection_random = time.time()
        OrderedList_selection = selection(list_random_numbers_selection[j], OrderedList)
        tf_selection_random = time.time()

        time_selection_random = "{:.3f}".format(tf_selection_random - t0_selection_random)
        time_selection.append(float(time_selection_random))

        # quicksort
        OrderedList = ['' for i in range(len(list_random_numbers_quicksort[j]))]
        t0_quicksort_random = time.time()
        OrderedList_quicksort = QuickSort(list_random_numbers_quicksort[j], OrderedList)#quicksort(list_random_numbers_quicksort[j], len(list_random_numbers_quicksort[j]))#QuickSort(list_random_numbers_quicksort[j], OrderedList)
        #arr = quicksort(list_random_numbers_quicksort[j])
        tf_quicksort_random = time.time()

        time_quicksort_random = "{:.3f}".format(tf_quicksort_random - t0_quicksort_random)
        time_quicksort.append(float(time_quicksort_random))

        # mergesort
        t0_mergesort_random = time.time()
        OrderedList_mergesort = mergesort(list_random_numbers_mergesort[j])
        tf_mergesort_random = time.time()

        time_mergesort_random = "{:.3f}".format(tf_mergesort_random - t0_mergesort_random)
        time_mergesort.append(float(time_mergesort_random))

        # insertion
        t0_insertion_random = time.time()
        OrderedList_insertion = insertion(list_random_numbers_insertion[j])
        tf_insertion_random = time.time()

        time_insertion_random = "{:.3f}".format(tf_insertion_random - t0_insertion_random)
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

# escrevendo os resultados em um arquivo de texto
f = open("results.out", "w")
for k in range(len(n)):
    f.write("=======================================================" + "\n\n")
    f.write("N = " + str(n[k]) + "\n\n")

    f.write("RANDOM" + "\n\n")

    f.write("Selection/ Mergesort / Quicksort / Insertion" + "\n\n")

    random_selection.append(time_selection[3*k])
    random_mergesort.append(time_mergesort[3*k])
    random_quicksort.append(time_quicksort[3*k])
    random_inserction.append(time_insertion[3*k])

    f.write(str(time_selection[3*k]) + " / " + str(time_mergesort[3*k]) + " / " + str(time_quicksort[3*k]) + " / " + str(time_insertion[3*k]) + "\n\n")

    f.write("CRESCENT" + "\n\n")

    f.write("Selection/ Mergesort / Quicksort / Insertion" + "\n\n")

    crescent_selection.append(time_selection[3*k+1])
    crescent_mergesort.append(time_mergesort[3*k+1])
    crescent_quicksort.append(time_quicksort[3*k+1])
    crescent_inserction.append(time_insertion[3*k+1])

    f.write(str(time_selection[3*k + 1]) + " / " + str(time_mergesort[3*k + 1]) + " / " + str(time_quicksort[3*k + 1]) + " / " + str(time_insertion[3*k + 1]) + "\n\n")

    f.write("DECRESCENTE" + "\n\n")

    f.write("Selection/ Mergesort / Quicksort / Insertion" + "\n\n")

    decrescente_selection.append(time_selection[3*k+2])
    decrescente_mergesort.append(time_mergesort[3*k+2])
    decrescente_quicksort.append(time_quicksort[3*k+2])
    decrescente_inserction.append(time_insertion[3*k+2])

    f.write(str(time_selection[3*k + 2]) + " / " + str(time_mergesort[3*k + 2]) + " / " + str(time_quicksort[3*k + 2]) + " / " + str(time_insertion[3*k + 2]) + "\n\n")
f.close()

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