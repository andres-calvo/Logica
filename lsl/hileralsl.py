from lsl import listaEnlazada
# replace,borrar,insertar,concat

class hileraLSL(listaEnlazada):
    def __init__(self):
        pass 
    def subHilera(self,i,j):
        nuevaHilera = hileraLSL()
        n = self.length()
        if (i < 0  or  i > n):
            print("parámetro i errado")
            return None
        if (j < 0  or j > n - i + 1):
            print("parámetro j errado")
            return None
        for k in range(i, i + j):
            nodoAinsertar = self.get(k)
            nuevaHilera.append(nodoAinsertar.data)
               
        return nuevaHilera

    def posicion(self,letra):
        contador=0
        for i in range (self.length()):
            if self.get(i).data != letra:
                contador+=1
            else:
                return contador    


l = hileraLSL()
l.append("y")
l.append("x")
l.append("b")
l.append("a")
# l.display()
l2 = l.subHilera(1,2)
l2.display()
# #print(l.posicion("y"))