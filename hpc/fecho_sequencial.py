from primitivas import *
import time


def proximo(pontos, p0, v):
    id_p0 = pontos.index(p0)
    # Menor angulo de alpha corresponde ao maior cosseno de alpha
    # Forcando o primeiro valor para a comparacao
    cos_alpha_maximo = -2

    p = None

    for i in range(len(pontos)):
        if (i != id_p0):
            # vetor entre o ponto i e o ponto de referencia p0
            vi = diferenca_vetorial(pontos[i], p0)
            # cosseno do vetor vi e o vetor v
            cos_alpha = produto_escalar(vi, v) / (norma(vi) * norma(v))
            if cos_alpha > cos_alpha_maximo:
                cos_alpha_maximo = cos_alpha
                p = pontos[i]
                id = i
            if cos_alpha == cos_alpha_maximo:
                vi_old = diferenca_vetorial(pontos[id], p0)
                norma_vi_old = norma(vi_old)
                vi_new = diferenca_vetorial(pontos[i], p0)
                norma_vi_new = norma(vi_new)
                if norma_vi_new > norma_vi_old:
                    p = pontos[i]
                    id = i

    if (p == None):
        print("Erro na funcao proximo\n")
        exit()
    else:
        return p

def fecho_convexo_sequencial(data_x, data_y):

    #par ordenado
    pontos = [(data_x[i], data_y[i]) for i in range(len(data_x))]
    
    #tempo inicial
    t0=time.time() 

    # pegar pontos de menor ordenada
    menor_y = pontos[0][1]
    aux = []
    for i in range(1, len(pontos)):
        y = pontos[i][1]
        if (y < menor_y):
            aux = []
            menor_y = y
            aux.append(pontos[i])
        elif (y == menor_y):
            aux.append(pontos[i])

    # dos pontos de menores ordenadas pegar o de menor abcissa
    menor_x = aux[0][0]
    for i in range(1, len(aux)):
        x = pontos[i][0]
        if (x < menor_x):
            menor_x = x

    # vetor com os pontos do fecho convexo
    fecho = []
    
    #primeiro ponto pertencente ao fecho
    p0 = (menor_x, menor_y)
    fecho.append(p0)
    id = pontos.index(p0)

    # proximo ponto tendo como referencia o giro de uma reta horizontal
    p1 = proximo(pontos, p0, (1, 0))
    fecho.append(p1)
    id_p = pontos.index(p1)

    # proximos pontos seguindo a ideia do algorimo de jarvis
    i = 1
    while (id != id_p):
        V = diferenca_vetorial(fecho[i], fecho[i - 1])
        next_p = proximo(pontos, fecho[i], V)
        fecho.append(next_p)
        id_p = pontos.index(next_p)
        i = i + 1

    #tempo final
    t1 = time.time() 
    
    #separacao do par ordenado 
    fecho_x = [fecho[i][0] for i in range(len(fecho))]
    fecho_y = [fecho[i][1] for i in range(len(fecho))]

    return t1-t0, fecho_x, fecho_y
