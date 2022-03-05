from lsl import listaEnlazada
from lsl import node
# subHilera,replace,borrar,insertar,concat,posicion

class hileraLSL(listaEnlazada):
    def __init__(self):
          self.head=node()  #Acá se crea este nodo para poder acceder al primer nodo de la listaEnlazada
    def subHilera(self,i,j):
        nuevaHilera = hileraLSL()
        n = self.length()
        if (i < 0  or  i > n):
            print("parámetro i errado")
            return None
        if (j < 0  or j > n - i + 1):
            print("parámetro j errado")
            return None
        for k in range(i, i + j+2):
            nuevaHilera.append(self.get(k))
               
            
        return nuevaHilera

    def posicion(letra):
        contador=0
        for i in range (self.longitud()):
            


l = hileraLSL()
l.append("y")
l.append("x")
l.append("b")
l.append("a")
# l.display()
l2 = l.subHilera(3,1)
l2.display()