import time
import numpy
from Order import *


#Tamanho da lista
#n = 10     #lista com 10 elementos
#n = 100    #lista com 100 elementos
#n = 1000   #lista com 1000 elementos
#n = 10000  #lista com 10000 elementos
#n = 100000 #lista com 100000 elementos
#n = 1000000 #lista com 1000000 elementos#
n = 100000000 #lista com 100000000 elementos

#lista de numeros aleatorios
random_numbers = numpy.random.uniform(size=n).tolist()
OrderedList= ['' for i in range(len(random_numbers))]  #vetor vazio para guardar os dados ordenados

#Lista em ordem crescente
random_numbers_crescente = sorted(random_numbers)

#Lista em ordem decrescente
random_numbers_decrescente  = sorted(random_numbers,reverse=True)

######################### selection ################################################
#ordenando
#t0_selection_random=time.time()
#OrderedList_selection = selection(random_numbers,OrderedList)
#tf_selection_random=time.time()
#
#time_selection_random = "{:.3f}".format(tf_selection_random-t0_selection_random)
#print("time selection random: " + time_selection_random + "\n")

######################### quicksort ################################################
#ordenando
#t0_quicksort_random=time.time()
#OrderedList_quicksort = QuickSort(random_numbers_crescente,OrderedList)
#tf_quicksort_random=time.time()
##
#time_quicksort_random = "{:.3f}".format(tf_quicksort_random-t0_quicksort_random)
#print("time quicksort random crescente: " + time_quicksort_random + "\n")


######################### mergesort ################################################
#ordenando
t0_mergesort_random=time.time()
OrderedList_mergesort = mergesort(random_numbers_crescente)
tf_mergesort_random=time.time()
##
time_mergesort_random = "{:.3f}".format(tf_mergesort_random-t0_mergesort_random)
print("time mergesort random crescente: " + time_mergesort_random + "\n")

######################### insertion ################################################
#ordenando
t0_insertion_random=time.time()
OrderedList_insertion = mergesort(random_numbers_crescente)
tf_insertion_random=time.time()
##
time_insertion_random = "{:.3f}".format(tf_insertion_random-t0_insertion_random)
print("time mergesort random crescente: " + time_insertion_random + "\n")