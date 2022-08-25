#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function
import numpy as np
import pyopencl as cl
import time
from primitivas import *

def fecho_convexo_com_open_cl(x_np, y_np):

    t0=time.time()

    #pegar um ponto da lista de menor ordenada e menor abscissa
    id_p = None
    menor_y = y_np[0]
    menor_x = x_np[0]

    for i in range(1,len(y_np)):

        if(y_np[i]<menor_y):
            menor_y = y_np[i]
            menor_x = x_np[i]
            id_p = i

        elif(y_np[i]==menor_y):
            if(x_np[i]<menor_x):
                menor_y = y_np[i]
                menor_x = x_np[i]
                id_p = i

    if(id_p == None):
        print("Erro para definir o ponto inicial\n")
        exit()
    else:
        if(((menor_y != y_np[id_p])) and (menor_x != x_np[id_p])):
            print("Erro para definir o ponto inicial\n")
            exit()

    #vetor com os pontos do fecho convexo
    fecho_x = []; fecho_y = []

    #ponto inicial
    p0_x = menor_x; p0_y = menor_y

    #ponto inicial pertence ao fecho
    fecho_x.append(p0_x); fecho_y.append(p0_y)

    #vetor auxiliar para criar o ponto base
    x_aux_np = (np.array([fecho_x[0]]*len(x_np))).astype(np.float32)
    y_aux_np = (np.array([fecho_y[0]]*len(x_np))).astype(np.float32)

    #vetor auxiliar para criar a reta suporte
    reta_x_aux_np = (np.array([1]*len(x_np))).astype(np.float32)
    reta_y_aux_np = (np.array([0]*len(x_np))).astype(np.float32)

    #criacao do contexto
    ctx = cl.create_some_context(0)
    queue = cl.CommandQueue(ctx)

    mf = cl.mem_flags

    #conjuntos de pontos
    x_g = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=x_np)
    y_g = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=y_np)

    #ponto base
    x_aux_g = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=x_aux_np)
    y_aux_g = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=y_aux_np)

    #reta suporte
    reta_x_aux_g = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=reta_x_aux_np)
    reta_y_aux_g = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=reta_y_aux_np)


    prg = cl.Program(ctx, """
    
    __kernel void cosseno(
        __global const float *x_base_g, __global const float *y_base_g, __global const float *x_reta_suporte_g, __global const float *y_reta_suporte_g,__global const float *x_g, __global const float *y_g, __global float *res_g)
    {
      int gid = get_global_id(0);
      
      //fazer a diferenca vetorial entre o ponto pi com o ponto base, criando um vetor (vi)
      float vi_x = x_g[gid]-x_base_g[gid];
      float vi_y = y_g[gid]-y_base_g[gid];
      
      
      //produto interno entre vi e a reta suporte
      float prod_interno = vi_x*x_reta_suporte_g[gid] + vi_y*y_reta_suporte_g[gid];
    
      //norma dos vetores
      float norma_vi = sqrt((pow(vi_x,2)+pow(vi_y,2)));
      float norma_v = sqrt(pow(x_reta_suporte_g[gid],2)+pow(y_reta_suporte_g[gid],2));
    
      //calculo do cosseno
      res_g[gid] = prod_interno/(norma_vi*norma_v);
    
      //quando encontrar o mesmo ponto, atribui o valor de -2 (qualquer cosseno ira ser maior que -2)
      if(norma_vi==0){
        res_g[gid] = -2;
      }
    
    }
    
    
    """).build()


    #proximo ponto em relacao a p0 e reta horizontal
    res_g = cl.Buffer(ctx, mf.WRITE_ONLY, x_np.nbytes)

    prg.cosseno(queue, x_np.shape, None, x_aux_g,y_aux_g,reta_x_aux_g,reta_y_aux_g,x_g,y_g,res_g)

    #inicializa o vetor com o resultado (valores aleatorios)
    res_np = np.empty_like(x_np)

    #atribui os valores da soma na variavel de resultado
    cl.enqueue_copy(queue, res_np, res_g)

    def getID(res_np, p0, data_x, data_y):
        #encontrar o proximo ponto (maior valor do cosseno)
        cosseno_max = res_np[0]
        id = 0
        for i in range(1,len(res_np)):
            if(res_np[i]>cosseno_max):
                cosseno_max = res_np[i]
                id = i
            elif(res_np[i]==cosseno_max):
                vi_old = diferenca_vetorial((data_x[id], data_y[id]), p0)
                norma_vi_old = norma(vi_old)
                vi_new = diferenca_vetorial((data_x[i], data_y[i]), p0)
                norma_vi_new = norma(vi_new)
                if norma_vi_new > norma_vi_old:
                    id = i
        return id

    id = getID(res_np, (fecho_x[0], fecho_y[0]), x_np, y_np)

    #proximo ponto pertence ao fecho convexo
    fecho_x.append(x_np[id]); fecho_y.append(y_np[id])

    #criar um while (ate id ser diferente id_p (ponto inicial do fecho convexo))
    i = 1
    while(id != id_p):
        #vetor auxiliar para criar o ponto base

        x_aux_np = (np.array([fecho_x[i]]*len(x_np))).astype(np.float32)
        y_aux_np = (np.array([fecho_y[i]]*len(x_np))).astype(np.float32)
        x_aux_g = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=x_aux_np)
        y_aux_g = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=y_aux_np)

        #vetor auxiliar para criar a reta suporte
        V = [fecho_x[i]-fecho_x[i-1],fecho_y[i]-fecho_y[i-1]]
        reta_x_aux_np = (np.array([V[0]]*len(x_np))).astype(np.float32)
        reta_y_aux_np = (np.array([V[1]]*len(x_np))).astype(np.float32)
        reta_x_aux_g = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=reta_x_aux_np)
        reta_y_aux_g = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=reta_y_aux_np)

        res_g = cl.Buffer(ctx, mf.WRITE_ONLY, x_np.nbytes)

        prg.cosseno(queue, x_np.shape, None, x_aux_g,y_aux_g,reta_x_aux_g,reta_y_aux_g,x_g,y_g,res_g)

        #inicializa o vetor com o resultado (valores aleatorios)
        res_np = np.empty_like(x_np)

        #atribui os valores da soma na variavel de resultado
        cl.enqueue_copy(queue, res_np, res_g)

        #pega o id do ponto
        id = getID(res_np, (fecho_x[i], fecho_y[i]), x_np, y_np)

        #proximo ponto pertence ao fecho convexo
        fecho_x.append(x_np[id]); fecho_y.append(y_np[id])

        i=i+1

    tf=time.time()

    return tf-t0, fecho_x, fecho_y
