def soma_vetorial(vector_x,vector_y):
    n_vector_x = len(vector_x)
    n_vector_y = len(vector_y)

    vector_z = []

    if(n_vector_x != n_vector_y):
        print("Vetores de tamanhos diferentes")
        exit()
    else:
        for i in range(n_vector_x):
            vector_z.append(vector_x[i]+vector_y[i])
    
    return vector_z

def multiplica_escalar(l,vector):
    n_vector = len(vector)
    vector_z = []
    for i in range(n_vector):
        vector_z.append(l*vector[i])

    return vector_z

def produto_escalar(vector_x,vector_y):
    n_vector_x = len(vector_x)
    n_vector_y = len(vector_y)

    soma = 0

    if(n_vector_x != n_vector_y):
        print("Vetores de tamanhos diferentes")
        exit()
    else:
        for i in range(n_vector_x):
            soma = soma + vector_x[i] * vector_y[i]
    
    return soma

def norma(vector):
    n_vector = len(vector)
    soma = 0
    for i in range(n_vector):
        soma = soma + (vector[i])**2

    return (soma)**(1/2)

def distancia(point_a,point_b):
    n_point_a = len(point_a)
    n_point_b = len(point_b)

    dist = None

    if(n_point_a != n_point_b):
        print("Vetores de tamanhos diferentes")
        exit()
    else:
        point_b = multiplica_escalar(-1,point_b)
        dist = soma_vetorial(point_a,point_b)
        return norma(dist)

def produto_vetorial(vector_x,vector_y):
    n_vector_x = len(vector_x)
    n_vector_y = len(vector_y)

    vector_z = []

    if(n_vector_x != n_vector_y):
        print("Vetores de tamanhos diferentes")
        exit()
    
    else:
        if(n_vector_x == 2 or n_vector_y ==2):
            vector_z.append(0)
            vector_z.append(0)
            vector_z.append(vector_x[0]*vector_y[1]-vector_x[1]*vector_y[0])

        if(n_vector_x == 3 or n_vector_y ==3):
            vector_z.append(vector_x[1]*vector_y[2]-vector_x[2]*vector_y[1])
            vector_z.append(vector_x[2]*vector_y[0]-vector_x[0]*vector_y[2])
            vector_z.append(vector_x[0]*vector_y[1]-vector_x[1]*vector_y[0])
    
    return vector_z