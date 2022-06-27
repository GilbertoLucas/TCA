import matplotlib.pyplot as plt
from primitivas import pseudo_angulo


def verifica_vertice(p1, P):
    # Calcula as coordenadas baricentricas do conjunto de pontos
    x_total = 0
    y_total = 0
    for i in range(len(P)):
        x_total += P[i][0]
        y_total += P[i][1]

    x_media = x_total / len(P)
    y_media = y_total / len(P)

    # Y equivale a um vetor que liga os pontos p1 e o baricentro (Esta é uma forma de referenciar os pseudo-angulos
    # calculados e evitar erros ao usar apenas o pseudo-angulo de X que será mostrado adiante)
    Y = [p1[0] - x_media, p1[1] - y_media]

    # Variável auxiliar para armazenar os pseudo-angulos
    pa = []

    # Verificando o pseudo-angulo dos pontos em relação ao vértice p1 em estudo
    for i in range(len(P)):

        if p1[0] != P[i][0] or p1[1] != P[i][1]:
            # X equivale a um vetor que liga os pontos de P e o vértice p1 em estudo. Assim, tem-se os angulos em relação
            # ao ponto p1 e não ao eixo x
            X = [P[i][0] - p1[0], P[i][1] - p1[1]]

            # Calculando a diferença entre os pseudo-angulos de X e Y
            if pseudo_angulo(X) - pseudo_angulo(Y) < 0:
                aux = pseudo_angulo(X) - pseudo_angulo(Y) + 8  # Soma 360º
            else:
                aux = pseudo_angulo(X) - pseudo_angulo(Y)  # Continua normalmente

            # Adiciona o pseudo-angulo à variável auxiliar
            pa.append(aux)
        else:
            pass

    # Verifica os pseudo-ângulos mínimo e máximo calculados
    pa_min = min(pa)
    pa_max = max(pa)

    # Verifica se estes são menores que 180º, ou seja, se encontram em um mesmo semi-plano
    if (pa_max - pa_min) <= 4:
        return True
    else:
        return False


# Conjunto de pontos
P = [[0,0], [3, -3.1], [5, -1], [4, 3], [4, 5], [0, 6], [-6, 4.1], [-3, -2]]
vertices = []
x_vertice = []
y_vertice = []
x_ponto = []
y_ponto = []
for i in range(len(P)):
    vertices.append(verifica_vertice(P[i], P))
    if verifica_vertice(P[i], P) is True:
        x_vertice.append(P[i][0])
        y_vertice.append(P[i][1])
    else:
        x_ponto.append(P[i][0])
        y_ponto.append(P[i][1])

plt.plot(x_vertice, y_vertice, 'ro', label="Vértice")
plt.plot(x_ponto, y_ponto, 'go')
plt.legend()
plt.show()
