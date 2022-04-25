


class order(object):
    def __init__(self) -> None:
        pass
    
    def selection(self,lista):
        x = lista

        N = len(x)

        for i in range(N-1):

            id_menor = i

            for j in range(i+1,N):
                if(x[j] < x[id_menor]):
                    id_menor = j


            aux = x[i]
            x[i] = x[id_menor]
            x[id_menor] = aux
    
