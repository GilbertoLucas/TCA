from primitivas import*

p1=[5,3]
p2=[1,4]
p3=[-2,4]
p4=[-4,3]
p5=[-5,1]
p6=[-5,-2]
p7=[-2,0]
p8=[7,-1]
p9=[8,0]


poligono = [p1,p2,p3,p4,p5,p6,p7,p8,p9]

if(len(poligono)<3):
    print("Poligono deve ter no minimo 3 pontos\n")
    exit()

else:
    convexo = True
    soma_areas = 0

    for i in range(len(poligono)-2):
        area = area_3pontos(poligono[i],poligono[i+1],poligono[i+2])
        soma_areas = soma_areas + area
        if(area<0):
            convexo = False
            print("Nao Convexo\n")
            exit()
    
    #ultimos 2 triangulos 
    a1 = area_3pontos(poligono[i+1],poligono[i+2],poligono[0])
    a2 = area_3pontos(poligono[i+2],poligono[0],poligono[1])
    if(a1<0 or a2 <0):
        convexo = False
        print("Nao Convexo\n")
        exit()

    soma_areas = soma_areas + a1 + a2

    if(soma_areas != 0):
        print("Convexo\n")
    else:
        print("Pontos Colineares\n")
