from lsl.lsl import listaEnlazada
from ldl import LDL
class ColaLSL(listaEnlazada):
    def __init__(self) -> None:
        super().__init__()


    def esVacia(self):
        return  self.primero==None
        
    def encolar(self,elemento):
        self.append(elemento)
        return
    def desencolar(self):
        if self.esVacia():
            print("La cola esta vacia")
            return
        self.desconectar(self.primero,None)
        dato=self.primero.retornaDato()
        return dato
class ColaLDL(LDL):
    def __init__(self):
        super().__init__()
    
    def esVacia(self):
        return  self.primero==None
        
    def encolar(self,elemento):
        self.append(elemento)
        return
    def desencolar(self):
        if self.esVacia():
            print("La cola esta vacia")
            return
        self.desconectar(self.primero,None)
        dato=self.primero.retornaDato()
        return dato
    
myCulo = ColaLDL()
myCulo.encolar(1)
myCulo.encolar(2)
myCulo.encolar(5)
myCulo.encolar(3)
myCulo.encolar(4)
myCulo.display()
myCulo.desencolar()
myCulo.display()
myCulo.desencolar()
myCulo.display()
myCulo.desencolar()
myCulo.display()

# head -> 3  4   5