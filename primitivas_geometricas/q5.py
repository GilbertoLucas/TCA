from primitivas import *
import matplotlib.pyplot as plt


def triangulos_disjuntos(vertices_triangulo_1, vertices_triangulo_2):

    # Vertices p1, p2, p3 do primeiro triângulo
    p1, p2, p3 = vertices_triangulo_1[0], vertices_triangulo_1[1], vertices_triangulo_1[2]

    # Definindo os PONTOS dos segmentos de reta do triangulo 2 com vertices q1, q2  e q3
    segmento_reta_q1q2 = [vertices_triangulo_2[0], vertices_triangulo_2[1]]
    segmento_reta_q2q3 = [vertices_triangulo_2[1], vertices_triangulo_2[2]]
    segmento_reta_q1q3 = [vertices_triangulo_2[0], vertices_triangulo_2[2]]

    # Uniao dos segmentos em um vetor
    segmentos_reta_triangulo_2 = [segmento_reta_q1q2, segmento_reta_q2q3, segmento_reta_q1q3]

    # Variável auxiliar para armazenar os dados sobre cada vertice do triangulo
    # 1 segmento de reta totalmente fora do triangulo
    # 2 segmento de reta dentro do triangulo
    aux = []

    for h in range(3):
        # Definindo o segmento de reta do triangulo q1q2q3
        pontos_segmento_reta = segmentos_reta_triangulo_2[h]

        # Avaliando o pontos "A" de cada segmento de reta do triangulo q1q2q3 (vide questão 4)
        A = pontos_segmento_reta[0]

        # Areas
        A_total = area_3pontos(p1, p2, p3)
        A1 = area_3pontos(A, p2, p3)
        A2 = area_3pontos(p1, A, p3)
        A3 = area_3pontos(p1, p2, A)

        # Coordenadas baricentricas em relacao a p1-p2-p3
        alfa1 = A1 / A_total
        alfa2 = A2 / A_total
        alfa3 = A3 / A_total

        # Avaliando o ponto "B" de cada segmento de reta do triangulo q1q2q3 (vide questão 4)
        B = pontos_segmento_reta[1]

        # Areas
        B_total = area_3pontos(p1, p2, p3)
        B1 = area_3pontos(B, p2, p3)
        B2 = area_3pontos(p1, B, p3)
        B3 = area_3pontos(p1, p2, B)

        # Coordenadas baricentricas em relacao a p1-p2-p3
        beta1 = B1 / B_total
        beta2 = B2 / B_total
        beta3 = B3 / B_total

        # Segmento de reta completamente fora do triangulo
        if (alfa1 < 0 and beta1 < 0) or (alfa2 < 0 and beta2 < 0) or (alfa3 < 0 and beta3 < 0):
            aux.append("1")
        else:
            aux.append("2")

    if aux == ['1', '1', '1']:
        print("Triângulos disjuntos")
    else:
        print("Triângulos não disjuntos")


# Teste 1 - não disjuntos
vertices_triangulo_1 = [[1, -3], [3, 2], [-3, 1]]
vertices_triangulo_2 = [[1, -3], [15, 17], [15, 17]]
triangulos_disjuntos(vertices_triangulo_1, vertices_triangulo_2)

# Teste 1 - disjuntos
vertices_triangulo_1 = [[1, -3], [3, 2], [-3, 1]]
vertices_triangulo_2 = [[15, 17], [15, 17], [15, 17]]
triangulos_disjuntos(vertices_triangulo_1, vertices_triangulo_2)