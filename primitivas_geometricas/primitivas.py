#Funcoes elementares
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

#Funcoes auxiliares

#Questao 1
def pseudo_angulo(X):
    n = len(X)
    if(n!=2):
        print("Vetor deve ser 2D\n")
        exit()
    else:
        x = X[0]
        y = X[1]

        if(y>0):  
            if(x>0):                        #Caso 1  (Primeiro Quadrante)
                if(x>=y):   
                    return y/x              #Caso 1.1
                else:
                    return 2 - x/y          #Caso 1.2
            elif(x==0):
                return 2                    #Caso 1.3  (Aresta Vertical Superior)
            
            else:                           #Caso 2    (Segundo Quadrante)
                if(-x<=y):
                    return 2 + (-x)/y       #Caso 2.1
                else:
                    return 4 - y/(-x)       #Caso 2.2
        
        
        elif(y==0):                         
            if(x>0):
                return 8                    #Caso 4.3  (Aresta Horizontal Direita)
            elif(x==0):
                return None                 #Vetor Nulo
            else:
                return 4                    #Caso 2.3  (Aresta Horizontal Esquerda)


        else:
            if(x<0):                        #Caso 3    (Terceiro Quadrante)
                if((-x)>=(-y)):
                    return 4 + (-y)/(-x)    #Caso 3.1
                else:
                    return 6 - (-x)/(-y)    #Caso 3.2
            
            elif(x==0):
                return 6                    #Caso 3.3  (Aresta Vertical Inferior)
            
            else:                           #Caso 4    (Quarto Quadrante)
                if(x<=(-y)):
                    return 6 + x/(-y)       #Caso 4.1
                else:
                    return 8 - (-y)/x       #Caso 4.2


def area_3pontos(p1,p2,p3):
    n1 = len(p1)
    n2 = len(p2)
    n3 = len(p3)
    if(n1 != 2):
        print("Ponto 1 deve ser 2D\n")
        exit()
    elif(n2 != 2):
        print("Ponto 2 deve ser 2D\n")
        exit()
    elif(n3 != 2):
        print("Ponto 3 deve ser 2D\n")
        exit()
    else:
        x1 = p1[0]; y1=p1[1]
        x2 = p2[0]; y2=p2[1]
        x3 = p3[0]; y3=p3[1]
        return (x1*y2 - x2*y1 + x2*y3 - x3*y2 + x3*y1 - x1*y3)/2