class vertice (object):
    def __init__(self,x,y,z,aresta=None):
        self.x = x
        self.y = y
        self.z = z
        self.aresta = aresta
    
    def set_aresta(self,a):
        self.aresta = a

class face (object):
    def __init__(self):
        self.aresta = None

    def set_aresta(self,a):
        self.aresta = a

class aresta (object):
    def __init__(self,vertice1=None,vertice2=None,fccw=None,fcw=None,pccw=None,nccw=None,pcw=None,ncw=None):
        self.vertice_1 = vertice1
        self.vertice_2 = vertice2

        self.fccw = fccw
        self.fcw = fcw

        self.pccw = pccw
        self.nccw = nccw
        
        self.pcw = pcw
        self.ncw = ncw
    
    def set_pccw(self,a):
        self.pccw = a
    
    def set_nccw(self,a):
        self.nccw = a
    
    def set_pcw(self,a):
        self.pcw = a
    
    def set_ncw(self,a):
        self.ncw = a

class winged_edge(object):
    def __init__(self,vertices,arestas,faces):
        self.vertices = vertices
        self.arestas = arestas
        self.faces = faces