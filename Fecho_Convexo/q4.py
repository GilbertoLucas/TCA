from WingedEdge import *

#funcao para procurar vertices incidentes a face
def v_inc_face(vertices_incidentes,aresta_i,face_procurada):
    
    if((aresta_i.fccw == face_procurada) or (aresta_i.fcw == face_procurada)):
        if(aresta_i.vertice_1 not in vertices_incidentes):
            vertices_incidentes.append(aresta_i.vertice_1)
        elif(aresta_i.vertice_2 not in vertices_incidentes):
            vertices_incidentes.append(aresta_i.vertice_2)

#funcao para procurar vertices incidentes a outros vertices
def v_inc_vertice(vertices_incidentes,aresta_i,vertice_procurado):
    
    if((aresta_i.vertice_1 == vertice_procurado)):
        if(aresta_i.vertice_1 not in vertices_incidentes):
            vertices_incidentes.append(aresta_i.vertice_2)    
    
    elif((aresta_i.vertice_2 == vertice_procurado)):
        if(aresta_i.vertice_2 not in vertices_incidentes):
            vertices_incidentes.append(aresta_i.vertice_1)


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

for i in range(len(d.arestas)):
    A = d.arestas[i]
    v_inc_face(v_incidentes_face,A,d.faces[id_face])


#questao 4b encontrar todos os vertices incidentes a outro vertice
#id do vertice escolhido
id_vertice = 5
v_incidentes_vertice = []

for i in range(len(d.arestas)):
    A = d.arestas[i]
    v_inc_vertice(v_incidentes_vertice,A,d.vertices[id_vertice])
