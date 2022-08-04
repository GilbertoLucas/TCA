#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function
import numpy as np
import pyopencl as cl
import time
from primitivas import pseudo_angulo
import matplotlib.pyplot as plt
#import copy
#import random

# Tamanho dos vetores
n = [10, 100, 1000]
#n = [10000, 100000, 1000000, 10000000, 100000000]

# Vetor para armazenar os tempos
time_sequencial = []
time_paralelo_1 = []
time_paralelo_2 = []

#vetor para armazenar o menor pseudo angulo de cada metodo
menor_sequencial = []
menor_paralelo_1 = []
menor_paralelo_2 = []


#criacao do contexto: Intel(R) OpenCL HD Graphics
ctx1 = cl.create_some_context(1)
queue1 = cl.CommandQueue(ctx1)
mf1 = cl.mem_flags
prg1 = cl.Program(ctx1, """

__kernel void pseudo(__global const float *x_g, __global const float *y_g, __global float *res_g)
{
  int gid = get_global_id(0);


  if(y_g[gid] > 0){
    if(x_g[gid] > 0){                         //Caso 1  (Primeiro Quadrante)
      if( x_g[gid] >= y_g[gid]){
        res_g[gid] = y_g[gid]/x_g[gid];       //Caso 1.1  
      }else{
        res_g[gid] = 2 - x_g[gid]/y_g[gid];   //Caso 1.2
      }
    }else if (x_g[gid] == 0){
      res_g[gid] = 2;                         //Caso 1.3  (Aresta Vertical Superior)
    }else{									                  //Caso 2 (Segundo Quadrante)
		if(-x_g[gid]<=y_g[gid]){
			res_g[gid] = 2 + (-x_g[gid]/y_g[gid]);   //Caso 2.1
		}else{
			res_g[gid] = 4 - (y_g[gid]/(-x_g[gid])); //Caso 2.2
		}
	}
  }else if (y_g[gid]==0){
	  if(x_g[gid]>0){
		  res_g[gid] = 8;                           //Caso 4.3  (Aresta Horizontal Direita)
	  }else if (x_g[gid] == 0){
		  printf("%s", "Vetor Nulo");
		  res_g[gid] = NULL;                      //Vetor Nulo
	  }else{
		  res_g[gid] = 4;                           //Caso 2.3  (Aresta Horizontal Esquerda
	  }
  }else{
	  if(x_g[gid]<0){                                         //Caso 3    (Terceiro Quadrante)
		  if((-x_g[gid])>=(-y_g[gid])){
			  res_g[gid] = 4 + (-y_g[gid])/(-x_g[gid]);          //Caso 3.1
		  }else{
			  res_g[gid] = 6 - (-x_g[gid])/(-y_g[gid]);         //Caso 3.2
		  }
	  }else if(x_g[gid]==0){	
		  res_g[gid] = 6;                                     //Caso 3.3  (Aresta Vertical Inferior)
	  }else{                                                
		if(x_g[gid]<=(-y_g[gid])){                            //Caso 4    (Quarto Quadrante)
			res_g[gid] = 6 + x_g[gid]/(-y_g[gid]);              //Caso 4.1
		}else{
			res_g[gid] = 8 - (-y_g[gid])/x_g[gid];              //Caso 4.2
		}
	  }
  }

}


""").build()


#criacao do contexto: AMD Accelerated Parallel Processing
ctx2 = cl.create_some_context(1)
queue2 = cl.CommandQueue(ctx2)
mf2 = cl.mem_flags
prg2 = cl.Program(ctx2, """

__kernel void pseudo(__global const float *x_g, __global const float *y_g, __global float *res_g)
{
  int gid = get_global_id(0);


  if(y_g[gid] > 0){
    if(x_g[gid] > 0){                         //Caso 1  (Primeiro Quadrante)
      if( x_g[gid] >= y_g[gid]){
        res_g[gid] = y_g[gid]/x_g[gid];       //Caso 1.1  
      }else{
        res_g[gid] = 2 - x_g[gid]/y_g[gid];   //Caso 1.2
      }
    }else if (x_g[gid] == 0){
      res_g[gid] = 2;                         //Caso 1.3  (Aresta Vertical Superior)
    }else{									                  //Caso 2 (Segundo Quadrante)
		if(-x_g[gid]<=y_g[gid]){
			res_g[gid] = 2 + (-x_g[gid]/y_g[gid]);   //Caso 2.1
		}else{
			res_g[gid] = 4 - (y_g[gid]/(-x_g[gid])); //Caso 2.2
		}
	}
  }else if (y_g[gid]==0){
	  if(x_g[gid]>0){
		  res_g[gid] = 8;                           //Caso 4.3  (Aresta Horizontal Direita)
	  }else if (x_g[gid] == 0){
		  printf("%s", "Vetor Nulo");
		  res_g[gid] = NULL;                      //Vetor Nulo
	  }else{
		  res_g[gid] = 4;                           //Caso 2.3  (Aresta Horizontal Esquerda
	  }
  }else{
	  if(x_g[gid]<0){                                         //Caso 3    (Terceiro Quadrante)
		  if((-x_g[gid])>=(-y_g[gid])){
			  res_g[gid] = 4 + (-y_g[gid])/(-x_g[gid]);          //Caso 3.1
		  }else{
			  res_g[gid] = 6 - (-x_g[gid])/(-y_g[gid]);         //Caso 3.2
		  }
	  }else if(x_g[gid]==0){	
		  res_g[gid] = 6;                                     //Caso 3.3  (Aresta Vertical Inferior)
	  }else{                                                
		if(x_g[gid]<=(-y_g[gid])){                            //Caso 4    (Quarto Quadrante)
			res_g[gid] = 6 + x_g[gid]/(-y_g[gid]);              //Caso 4.1
		}else{
			res_g[gid] = 8 - (-y_g[gid])/x_g[gid];              //Caso 4.2
		}
	  }
  }

}


""").build()



for i in range(len(n)):
	#conjunto de pontos aleatorios
    x_np = np.random.rand(n[i]).astype(np.float32)
    y_np = np.random.rand(n[i]).astype(np.float32)


    #----------------------------resolucao da forma sequencial--------------------------------------------
    pseudo_a = []
    t0_sequencial=time.time()        #tempo inicial
    for i in range(n[i]):
      pseudo_a.append(pseudo_angulo([x_np[i],y_np[i]]))
    
    menor_seq = min(pseudo_a)  #menor valor da lista
    
    tf_sequencial = time.time()      #tempo final

    menor_sequencial.append(menor_seq)           #armazena o menor pseudo angulo para n pontos
    time_sequencial.append(tf_sequencial - t0_sequencial) #armazena o tempo da solucao para n pontos
    #----------------------------resolucao da forma sequencial--------------------------------------------




    #----------------------------resolucao da forma paralela 1 --------------------------------------------
    t0_paralelo_1=time.time()

    #cópia para o buffer
    x_g = cl.Buffer(ctx1, mf1.READ_ONLY | mf1.COPY_HOST_PTR, hostbuf=x_np)
    y_g = cl.Buffer(ctx1, mf1.READ_ONLY | mf1.COPY_HOST_PTR, hostbuf=y_np)
    res_g = cl.Buffer(ctx1, mf1.WRITE_ONLY, x_np.nbytes)

    #chama a função do kernel
    prg1.pseudo(queue1, x_np.shape, None, x_g,y_g, res_g)

    #inicializa o vetor com o resultado (valores aleatorios)
    res_np = np.empty_like(x_np)

    #atribui os valores da soma na variavel de resultado
    cl.enqueue_copy(queue1, res_np, res_g)

    #menor pseudo-ângulo
    menor_paralelo_1.append(min(res_np))

    tf_paralelo_1=time.time()
    time_paralelo_1.append(tf_paralelo_1 - t0_paralelo_1)
    #----------------------------resolucao da forma paralela 1--------------------------------------------


    #----------------------------resolucao da forma paralela 2 --------------------------------------------
    t0_paralelo_2=time.time()

    # cópia para o buffer
    x_g = cl.Buffer(ctx2, mf2.READ_ONLY | mf2.COPY_HOST_PTR, hostbuf=x_np)
    y_g = cl.Buffer(ctx2, mf2.READ_ONLY | mf2.COPY_HOST_PTR, hostbuf=y_np)
    res_g = cl.Buffer(ctx2, mf2.WRITE_ONLY, x_np.nbytes)

    # chama a função do kernel
    prg2.pseudo(queue2, x_np.shape, None, x_g,y_g, res_g)

    #inicializa o vetor com o resultado (valores aleatorios)
    res_np = np.empty_like(x_np)

    #atribui os valores da soma na variavel de resultado
    cl.enqueue_copy(queue2, res_np, res_g)

    # menor pseudo-ângulo
    menor_paralelo_2.append(min(res_np))

    tf_paralelo_2=time.time()
    time_paralelo_2.append(tf_paralelo_2 - t0_paralelo_2)
    #----------------------------resolucao da forma paralela 2--------------------------------------------


# escrevendo os resultados em um arquivo de texto
f = open("results.out", "w")
for i in range(len(n)):
    f.write("=======================================================" + "\n\n")
    f.write("N = " + str(n[i]) + "\n\n")
    
    f.write("Sequencial")
    f.write("\nMenor pseudo-angulo: {:.6f}".format(menor_sequencial[i]))
    f.write("\nTempo: {:.6f}\n".format(time_sequencial[i]))
    
    f.write("\nParalelo - Intel(R) UHD Graphics")
    f.write("\nMenor pseudo-angulo: {:.6f}".format(menor_paralelo_1[i]))
    f.write("\nTempo: {:.6f}\n".format(time_paralelo_1[i]))
    
    f.write("\nParalelo - NVIDIA GeForce GTX 1650")
    f.write("\nMenor pseudo-angulo: {:.6f}".format(menor_paralelo_2[i]))
    f.write("\nTempo: {:.6f}\n".format(time_paralelo_2[i]))
f.close()

#plt.plot(n, time_paralelo_1, '-d', label="Paralelo - Intel(R) UHD Graphics")
plt.plot(n, time_paralelo_2, '-x', label="Paralelo - NVIDIA GeForce GTX 1650")
plt.plot(n, time_sequencial, '-+', label="Sequencial")
plt.xticks(n)
plt.xlabel("Número de pontos")
plt.ylabel("Tempo (ms)")
#plt.yscale("log")
#plt.xscale("log")
plt.legend()
plt.grid()
plt.show()

plt.plot()
