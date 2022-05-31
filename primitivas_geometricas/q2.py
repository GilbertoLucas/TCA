from primitivas import *


def entre(u, v, w):
    # calculando o produto cruzado entre as coordenadas
    produto_cruzado_1 = u[0] * v[1]
    produto_cruzado_2 = u[1] * v[0]

    # tolerancia para verificar a condição de colinearidade
    tol = 1e-9

    # verificando se os vetores u e v são colineares
    if abs(produto_cruzado_1 - produto_cruzado_2) <= tol:
        return 0
    else:
        # calculando o pseudo-ângulo do vetor u
        pseudo_angulo_u = pseudo_angulo(u)

        # calculando o pseudo-ângulo do vetor v
        pseudo_angulo_v = pseudo_angulo(v)

        # calculando o pseudo-angulo do vetor w
        pseudo_angulo_w = pseudo_angulo(w)

        # Verificação de quem é maior entre u e v
        if pseudo_angulo_u > pseudo_angulo_v:
            # Caso da diferença entre os ângulo u e v ser convexa, além do vetor w entre v e u
            if (pseudo_angulo_u - pseudo_angulo_v < 4.0) and (pseudo_angulo_v < pseudo_angulo_w < pseudo_angulo_u):
                return 1

            # Caso da diferença entre os ângulo u e v não ser convexa, além do vetor w entre u e v
            elif (pseudo_angulo_u - pseudo_angulo_v > 4.0) and (pseudo_angulo_u < pseudo_angulo_w > pseudo_angulo_v):
                return 1

            # Caso de w fora da região convexa
            else:
                return 2
        else:
            # Caso da diferença entre os ângulo v e u ser convexa, além do vetor w entre u e v
            if (pseudo_angulo_v - pseudo_angulo_u < 4.0) and (pseudo_angulo_u < pseudo_angulo_w < pseudo_angulo_v):
                return 1

            # Caso da diferença entre os ângulo v e u não ser convexa, além do vetor w entre v e u
            elif (pseudo_angulo_v - pseudo_angulo_u > 4.0) and (pseudo_angulo_v < pseudo_angulo_w > pseudo_angulo_u):
                return 1

            # Caso de w fora da região convexa
            else:
                return 2

# Teste 1
u1, v1, w1 = [2.0, 4.0], [8.0, 16.0], [0.2, 0.5]
teste_1 = entre(u1, v1, w1)

# Teste 2
u2, v2, w2 = [-0.15, 1.0], [0.99, 1.0], [-0.1, 1.0]
teste_2 = entre(u2, v2, w2)

# Teste 3
u3, v3, w3 = [0.0, -1.0], [1.0, 1.0], [0.15, -1.0]
teste_3 = entre(u3, v3, w3)

# Teste 4
u4, v4, w4 = [0.0, -1.0], [1.0, 1.0], [-1.0, -1.0]
teste_4 = entre(u4, v4, w4)

########################################################################################################################

# Teste 5
v5, u5, w5 = [2.0, 4.0], [8.0, 16.0], [0.2, 0.5]
teste_5 = entre(u5, v5, w5)

# Teste 6
v6, u6, w6 = [-0.15, 1.0], [0.99, 1.0], [-0.1, 1.0]
teste_6 = entre(u6, v6, w6)

# Teste 7
v7, u7, w7 = [0.0, -1.0], [1.0, 1.0], [0.15, -1.0]
teste_7 = entre(u7, v7, w7)

# Teste 8
v8, u8, w8 = [0.0, -1.0], [1.0, 1.0], [-1.0, -1.0]
teste_8 = entre(u8, v8, w8)

########################################################################################################################

# Teste 9
v9, u9, w9 = [-0.15, 1.0], [0.99, 1.0], [-0.15, 1.0]
teste_9 = entre(u9, v9, w9)

# Teste 10
u10, v10, w10 = [1, 2], [2.5, 5], [1, 4]
teste_10 = entre(u10, v10, w10)

aux = 'Teste'
