from WingedEdge import *

#vertices (x,y,z)
v1 = vertice(1,0,0)
v2 = vertice(1,1,0)
v3 = vertice(1,1,1)
v4 = vertice(1,0,1)
v5 = vertice(0,0,0)
v6 = vertice(0,1,0)
v7 = vertice(0,1,1)
v8 = vertice(0,0,1)

#faces
f1 = face()
f2 = face()
f3 = face()
f4 = face()
f5 = face()
f6 = face()

#arestas (vertice1,vertice2,fccw,fcw)
a1 = aresta(v1,v2,f1,f5)
a2 = aresta(v2,v3,f1,f2)
a3 = aresta(v3,v4,f1,f6)
a4 = aresta(v4,v1,f1,f4)
a5 = aresta(v1,v5,f5,f4)
a6 = aresta(v2,v6,f2,f5)
a7 = aresta(v3,v7,f6,f2)
a8 = aresta(v4,v8,f4,f6)
a9 = aresta(v5,v6,f5,f3)
a10 = aresta(v6,v7,f2,f3)
a11 = aresta(v7,v8,f6,f3)
a12 = aresta(v8,v5,f4,f3)

#arestas incidentes nos vertices
v1.set_aresta(a1)
v2.set_aresta(a2)
v3.set_aresta(a3)
v4.set_aresta(a4)
v5.set_aresta(a9)
v6.set_aresta(a10)
v7.set_aresta(a11)
v8.set_aresta(a12)

#arestas incidentes nas faces
f1.set_aresta(a1)
f2.set_aresta(a2)
f3.set_aresta(a10)
f4.set_aresta(a12)
f5.set_aresta(a1)
f6.set_aresta(a8)

#arestas: pccw,nccw, pcw,fcw
a1.set_pccw(a4);  a1.set_nccw(a2);  a1.set_pcw(a6);   a1.set_ncw(a5)
a2.set_pccw(a1);  a2.set_nccw(a3);  a2.set_pcw(a7);   a2.set_ncw(a6)
a3.set_pccw(a2);  a3.set_nccw(a4);  a3.set_pcw(a8);   a3.set_ncw(a7)
a4.set_pccw(a3);  a4.set_nccw(a1);  a4.set_pcw(a5);   a4.set_ncw(a8)
a5.set_pccw(a1);  a5.set_nccw(a9);  a5.set_pcw(a12);  a5.set_ncw(a4)
a6.set_pccw(a2);  a6.set_nccw(a10); a6.set_pcw(a9);   a6.set_ncw(a1)
a7.set_pccw(a3);  a7.set_nccw(a11); a7.set_pcw(a10);  a7.set_ncw(a2)
a8.set_pccw(a4);  a8.set_nccw(a12); a8.set_pcw(a11);  a8.set_ncw(a3)
a9.set_pccw(a5);  a9.set_nccw(a6);  a9.set_pcw(a10);  a9.set_ncw(a12)
a10.set_pccw(a6); a10.set_nccw(a7); a10.set_pcw(a11); a10.set_ncw(a9)
a11.set_pccw(a7); a11.set_nccw(a8); a11.set_pcw(a12); a11.set_ncw(a10)
a12.set_pccw(a8); a12.set_nccw(a5); a12.set_pcw(a9);  a12.set_ncw(a11)

#montar a estrutura
a = [a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12]
v = [v1,v2,v3,v4,v5,v6,v7,v8]
f = [f1,f2,f3,f4,f5,f6]

d = winged_edge(v,a,f)

#questao 4a - encontrar todos os vertices incidentes a face
#id da face escolhida
id_face = 3
v_incidentes_face = []

#dois primeiros verticies sao incidentes a aresta ligada a face
v_incidentes_face.append(d.faces[id_face].aresta.vertice_1)
v_incidentes_face.append(d.faces[id_face].aresta.vertice_2)

#aresta inicial
a_0 = d.faces[id_face].aresta
#aresta vazia
a_i = aresta()  

cnt = 0 #(forca a entrada no loop)

while(a_i != a_0):
    
    if(cnt == 0):
        a_i = a_0
        cnt = 1

    #face procurada e' a face anti horaria da aresta(i)
    if(d.faces[id_face] == a_i.fccw):
        if(a_i.vertice_1 not in v_incidentes_face):
            v_incidentes_face.append(a_i.vertice_1)
        elif(a_i.vertice_2 not in v_incidentes_face):
            v_incidentes_face.append(a_i.vertice_2)
        
        #nova aresta e' a next do sentido anti horario
        a_i = a_i.nccw
    
    #face procurada e' a face horaria da aresta(i)
    elif(d.faces[id_face] == a_i.fcw):
        if(a_i.vertice_1 not in v_incidentes_face):
            v_incidentes_face.append(a_i.vertice_1)
        elif(a_i.vertice_2 not in v_incidentes_face):
            v_incidentes_face.append(a_i.vertice_2)
        
        #nova aresta e' a next do sentido anti horario
        a_i = a_i.ncw



#questao 4b encontrar todos os vertices incidentes a outro vertice
#id do vertice escolhido
id_vertice = 7
v_incidentes_vertice = []
aresta_incidente = d.vertices[id_vertice].aresta

#procura todos os vertices incidentes
if(d.vertices[id_vertice] == aresta_incidente.vertice_1):
    
    v_incidentes_vertice.append(aresta_incidente.vertice_2)
    
    if((aresta_incidente.pccw.vertice_1 == d.vertices[id_vertice]) and (aresta_incidente.pccw.vertice_2 not in v_incidentes_vertice ) ):
        v_incidentes_vertice.append(aresta_incidente.pccw.vertice_2)
    
    elif((aresta_incidente.pccw.vertice_2 == d.vertices[id_vertice]) and (aresta_incidente.pccw.vertice_1 not in v_incidentes_vertice )):
        v_incidentes_vertice.append(aresta_incidente.pccw.vertice_1)
    
    if((aresta_incidente.ncw.vertice_1 == d.vertices[id_vertice]) and (aresta_incidente.ncw.vertice_2 not in v_incidentes_vertice )):
        v_incidentes_vertice.append(aresta_incidente.ncw.vertice_2)
    
    elif((aresta_incidente.ncw.vertice_2 == d.vertices[id_vertice]) and (aresta_incidente.ncw.vertice_1 not in v_incidentes_vertice )):
        v_incidentes_vertice.append(aresta_incidente.ncw.vertice_1)

elif(d.vertices[id_vertice] == aresta_incidente.vertice_2):
    
    v_incidentes_vertice.append(aresta_incidente.vertice_1)
    
    if((aresta_incidente.pcw.vertice_1 == d.vertices[id_vertice]) and (aresta_incidente.pcw.vertice_2 not in v_incidentes_vertice ) ):
        v_incidentes_vertice.append(aresta_incidente.pcw.vertice_2)
    
    elif((aresta_incidente.pcw.vertice_2 == d.vertices[id_vertice]) and (aresta_incidente.pcw.vertice_1 not in v_incidentes_vertice )):
        v_incidentes_vertice.append(aresta_incidente.pcw.vertice_1)
    
    if((aresta_incidente.nccw.vertice_1 == d.vertices[id_vertice]) and (aresta_incidente.nccw.vertice_2 not in v_incidentes_vertice )):
        v_incidentes_vertice.append(aresta_incidente.nccw.vertice_2)
    
    elif((aresta_incidente.nccw.vertice_2 == d.vertices[id_vertice]) and (aresta_incidente.nccw.vertice_1 not in v_incidentes_vertice )):
        v_incidentes_vertice.append(aresta_incidente.nccw.vertice_1)
