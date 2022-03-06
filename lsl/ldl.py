from  lsl import listaEnlazada
from lsl import node
class dobleNodo(node):
    def __init__(self,data=None):
        self.data=data #Acá le agrego el dato al nodo
        self.next=None #Acá es a donde apunta el nodo, osea el siguiente elemento , se empieza desde null
        self.prev=None
    def retornaLi(self):
        return self.prev
    def asignaLi(self,liga):
        self.prev = liga
    def retornaLd(self):
        return self.next
    def asignaLd(self,liga):
        self.next = liga
        


class LDL(listaEnlazada):
    primero=None
    ultimo=None
    def __init__(self):
        pass
         
    #Funcion de agregar nodo a la lista al final:
    def append(self,data):
        new_node=dobleNodo(data)
        if self.primero == None:
            self.primero = new_node
            self.ultimo = new_node
            return
        cur=self.primero
        while cur.next != None:
            cur=cur.next
        new_node.asignaLi(cur)
        cur.asignaLd(new_node)
        if(self.ultimo != None):
            new_node.asignaLi(self.ultimo)
            self.ultimo.asignaLd(new_node)
            self.ultimo = new_node


    #  Borrar elemento de la lista pasando el index 
    
    def erase(self,index):
        if index >=self.length():
            print ("Error: index fuera del rango",index)
            return
        primeroActual = self.primero
        if index == 0:
            self.primero = primeroActual.retornaLiga()
            self.primero.prev = None
            return
        if index == self.length() -1:
            nodo = self.get(index)
            while nodo != self.ultimo:
                nodo.next = nodo.next
            nodo.next = None
        cur_idx=1
        cur_node=self.primero
        while True: # x y z
            last_node=cur_node
            cur_node=cur_node.next
            if cur_idx==index:
                cur_node.next.asignaLi(last_node.next)
                last_node.asignaLd(cur_node.next)
                return
            cur_idx +=1