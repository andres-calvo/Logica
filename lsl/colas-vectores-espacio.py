#
# crear: crea una cola vacía
# esVacia(): retorna verdadero si la cola está vacía, falso de lo contrario
# esLlena(): retorna verdadero si la cola está llena, falso de lo contrario
# encolar(d): inserta un dato d al final de la cola.
# desencolar(): remueve el primer elemento de la cola
# siguiente(): retorna el dato que se hall de primero en la cola.



class Cola:
    vector=[]
    longitud=0
    primero=0
    ultimo=0
    def __init__(self,longitud) -> None:
        for i in range(longitud):
            self.vector.append(None)
        self.longitud=longitud
        
    def siguiente(self):
        return self.vector[self.primero + 1]
    def esColaVacia(self):
        return self.primero == self.ultimo
    def encolar(self,elemento):
        self.ultimo = (self.ultimo + 1) % self.longitud
        if self.ultimo == self.primero : 
            self.colaLlena()
            return
        self.vector[self.ultimo]=elemento

    def colaLlena(self):
        self.ultimo = (self.ultimo + self.longitud - 1) % self.longitud
        print("La cola esta llena")
        #arreglar posicion ultimo
    def colaVacia(self):
        pass

    def desencolar(self):
        if self.primero == self.ultimo:
            self.colaVacia()
            print("La cola esta vacia")
            return 
        self.primero = (self.primero+1) % self.longitud
        elemento=self.vector[self.primero]
        
        self.vector[self.primero] = None
        return elemento    

myCola = Cola(5)
myCola.encolar(2)
myCola.encolar(3)
myCola.encolar(4)
myCola.encolar(5)

print(myCola.ultimo)

print(myCola.vector)

myCola.encolar(6)
myCola.encolar(7)
print("eliminado",myCola.desencolar())
print("eliminado",myCola.desencolar())
print("eliminado",myCola.desencolar())
myCola.encolar(1)
myCola.encolar(2)
# # print(myCola.ultimo)
print(myCola.vector)
# myCola.encolar(1)
# print(myCola.vector)


