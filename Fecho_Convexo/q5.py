from cv2 import norm
from primitivas import *
import numpy as np
import matplotlib.pyplot as plt



def proximo(p0,v):
    id_p0 = pontos.index(p0)
    #Menor angulo de alpha corresponde ao maior cosseno de alpha
    #Forcando o primeiro valor para a comparacao
    cos_alpha_maximo = -2
    
    p = None

    for i in range(len(pontos)):
        if(i != id_p0):
            #vetor entre o ponto i e o ponto de referencia p0
            vi = diferenca_vetorial(pontos[i],p0)
            #cosseno do vetor vi e o vetor v
            cos_alpha = produto_escalar(vi,v)/(norma(vi)*norma(v))
            if(cos_alpha > cos_alpha_maximo):
                cos_alpha_maximo = cos_alpha
                p = pontos[i]

    if(p == None):
        print("Erro na funcao proximo\n")
        exit()
    else:
        return p

#numero de pontos
n = 50

#lista randomica
lista = list(np.random.randint(25,475,size = 2*n))

#vetor com as coordenadas
pontos = []
for i in range(0,len(lista) - 1, 2):
    pontos.append([lista[i],lista[i+1]])


#teste com tres pontos colineares
#pontos = [[-3,1.5],[-1,0],[2.5,2.5],[-1,4],[1,-1],[-2,-2],[1,-2],[1.5,2],[0,-2]]

#pegar pontos de menor oordenada
menor_y = pontos[0][1]
aux = []
for i in range(1,len(pontos)):
    y = pontos[i][1]
    if(y<menor_y):
        aux = []
        menor_y = y
        aux.append(pontos[i])
    elif(y == menor_y):
        aux.append(pontos[i])

#dos pontos de menores ordenadas pegar o de menor abicissa 
menor_x = aux[0][0]
for i in range(1,len(aux)):
    x = pontos[i][0]
    if(x < menor_x):
        menor_x = x


#vetor com os pontos do fecho convexo
fecho = []

p0 = [menor_x,menor_y]
fecho.append(p0)
id = pontos.index(p0)

#proximo ponto tendo como referencia o giro de uma reta horizontal
p1 = proximo(p0,(1,0))
fecho.append(p1)
id_p = pontos.index(p1)

#proximos pontos seguindo a ideia do algorimo de jarvis
i = 1
while (id != id_p):
    V = diferenca_vetorial(fecho[i],fecho[i-1])
    next_p = proximo(fecho[i],V)
    fecho.append(next_p)
    id_p = pontos.index(next_p)
    i = i + 1

print("Pontos do fecho convexo:\n")
print(fecho)


#Plotar os pontos
x = []
y = []

for i in range(len(pontos)):
    x.append(pontos[i][0])
    y.append(pontos[i][1])


plt.plot( x, y, 'go') 
plt.axis([min(x)-abs(min(x)/10), max(x)+abs(max(x)/10), min(y)-abs(min(y)/10), max(y)+abs(max(y)/10)])
plt.show()


#Plotar o Fecho convexo
x_fecho = []
y_fecho = []
for i in range(len(fecho)):
    x_fecho.append(fecho[i][0])
    y_fecho.append(fecho[i][1])


plt.plot(x, y, 'go') 
plt.plot(x_fecho, y_fecho, 'ro')
plt.plot(x_fecho, y_fecho, color='red') 
plt.axis([min(x)-abs(min(x)/10), max(x)+abs(max(x)/10), min(y)-abs(min(y)/10), max(y)+abs(max(y)/10)])
plt.show()