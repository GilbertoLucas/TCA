import time
import numpy
from Order import *


#Tamanho da lista
#n = 10     #lista com 10 elementos
#n = 100    #lista com 100 elementos
#n = 1000   #lista com 1000 elementos
#n = 10000  #lista com 10000 elementos
n = 100000 #lista com 100000 elementos
#n = 1000000 #lista com 1000000 elementos


#lista de numeros aleatorios
random_numbers = numpy.random.uniform(size=n).tolist()

#Lista em ordem crescente
random_numbers_crescente = sorted(random_numbers)

#Lista em ordem decrescente
random_numbers_decrescente  = sorted(random_numbers,reverse=True)


######################### selection ################################################
#ordenando
t0_selection_random=time.time()
selection(random_numbers)
tf_selection_random=time.time()

time_selection_random = "{:.3f}".format(tf_selection_random-t0_selection_random)
print("time selection random: " + time_selection_random + "\n")


#ordenando
t0_selection_random_crescente = time.time()
selection(random_numbers_crescente)
tf_selection_random_crescente = time.time()

time_selection_random_crescente = "{:.3f}".format(tf_selection_random_crescente-t0_selection_random_crescente)
print("time selection random crescente: " + time_selection_random_crescente + "\n")

#ordenando
t0_selection_random_decrescente = time.time()
selection(random_numbers_decrescente)
tf_selection_random_decrescente = time.time()


time_selection_random_decrescente = "{:.3f}".format(tf_selection_random_decrescente-t0_selection_random_decrescente)
print("time selection random decrescente: " + time_selection_random_decrescente + "\n")


######################### quicksort (ainda testando) ################################################
#ordenando
#t0_quicksort_random=time.time()
#x_random = order().quicksort(random_numbers)
#tf_quicksort_random=time.time()
#
#time_quicksort_random = "{:.3f}".format(tf_quicksort_random-t0_quicksort_random)
#print("time quicksort random: " + time_quicksort_random + "\n")


#ordenando
#t0_quicksort_random_crescente = time.time()
#quicksort(random_numbers_crescente)
#tf_quicksort_random_crescente = time.time()
#
#time_quicksort_random_crescente = "{:.3f}".format(tf_quicksort_random_crescente-t0_quicksort_random_crescente)
#print("time quicksort random crescente: " + time_quicksort_random_crescente + "\n")
#
##ordenando
#t0_quicksort_random_decrescente = time.time()
#x_random_decrescente = order().quicksort(random_numbers_decrescente)
#tf_quicksort_random_decrescente = time.time()
#
#
#time_quicksort_random_decrescente = "{:.3f}".format(tf_quicksort_random_decrescente-t0_quicksort_random_decrescente)
#print("time quicksort random decrescente: " + time_quicksort_random_decrescente + "\n")
#
