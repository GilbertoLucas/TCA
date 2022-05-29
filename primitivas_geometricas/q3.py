from primitivas import*


#Vertices do triangulo
p1 = [1, -3]
p2 = [3, 2]
p3 = [-3, 1]

#Ponto a ser verificado
p =  [15, 17]

#Areas
A = area_3pontos(p1,p2,p3)
if(A == 0):
    print("Pontos sao colineares")
    exit()

A1 = area_3pontos(p,p2,p3)
A2 = area_3pontos(p1,p,p3)
A3 = area_3pontos(p1,p2,p)

#coordenadas baricentricas em relacao a p1-p2-p3
lambda1 = A1/A
lambda2 = A2/A
lambda3 = A3/A
l = [lambda1, lambda2, lambda3]    

#Processo de verificacao da posicao de p em relacao a p1-p2-p3
if(lambda1>0 and lambda2>0 and lambda3 >0):
    print("Ponto interior ao triangulo formado por p1-p2-p3")
    exit()
else:
    if(lambda1 == 0):
        if(lambda2 > 0 and lambda3 > 0):
            print("Fronteira p2-p3")
            exit()
        elif(lambda2 == 0):
            print("Ponto sobrepoe p3")
            exit()
        elif(lambda3 == 0):
            print("Ponto sobrepoe p2")
            exit()
        else:
            print("Ponto externo ao triangulo")
            exit()
    
    elif(lambda2 == 0):
        if(lambda1 > 0 and lambda3 > 0):
            print("Fronteira p1-p3")
            exit()
        elif(lambda1 == 0):
            print("Ponto sobrepoe p3")
            exit()
        elif(lambda3 == 0):
            print("Ponto sobrepoe p1")
            exit()
        else:
            print("Ponto externo ao triangulo")
            exit()

    elif(lambda3 == 0):
        if(lambda1 > 0 and lambda2 > 0):
            print("Fronteira p1-p2")
            exit()
        elif(lambda1 == 0):
            print("Ponto sobrepoe p2")
            exit()
        elif(lambda2 == 0):
            print("Ponto sobrepoe p1")
            exit()
        else:
            print("Ponto externo ao triangulo")
            exit()
    else:
        print("Ponto externo ao triangulo")
        exit()
