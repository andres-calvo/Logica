class node:
    def __init__(self,data=None):
        self.data=data #Acá le agrego el dato al nodo
        self.next=None #Acá es a donde apunta el nodo, osea el siguiente elemento , se empieza desde null
    def asignaDato(self,data):
        self.data = data
    def retornaDato(self):
        return self.data
    def retornaLiga(self):
        return self.next
    def asignaLiga(self,liga):
        self.next = liga
        


class listaEnlazada:
    primero=None
    ultimo=None
    def __init__(self):
        pass
         
    #Funcion de agregar nodo a la lista al final:
    def append(self,data):
        new_node=node(data)

        if self.primero == None:
            self.primero = new_node
            self.ultimo = new_node
            return
        cur=self.primero
        while cur.next != None:
            cur=cur.next
        cur.next=new_node
        if(self.ultimo != None):
            self.ultimo.asignaLiga(new_node)
            self.ultimo = new_node

    

    #Funcion para saber el length de la lista:
    def length(self):
        cur=self.primero
        total=0
        if(self.primero != None):
            total=1
        while cur.next != None:
            total +=1
            cur=cur.next        
        return total

    #Mostrar contenido de la lista:

    def display(self):
        elems=[]
        cur_node=self.primero
        while cur_node != None:
            elems.append(cur_node.data)
            cur_node=cur_node.next
        print(elems)

    # Extraer nodo de la lista 
    #  ej= objeto.get(valor)
    def get(self,index)->node:
        if index >=self.length():
            print ("Error: index fuera del rango",index)
            return None
        cur_idx=0
        cur_node=self.primero
        while True:
                if cur_idx==index: return cur_node
                cur_node=cur_node.next
                cur_idx +=1

    #  Borrar elemento de la lista pasando el index 
    
    def erase(self,index):
        if index >=self.length():
            print ("Error: index fuera del rango",index)
            return
        primeroActual = self.primero
        if index == 0:
            self.primero = primeroActual.retornaLiga()
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
                last_node.next= cur_node.next
                return
            cur_idx +=1

    def conectar(self, x:node, y:node):
        if(y == None):
            if(self.primero == None):
                self.ultimo = x
            else:
                x.asignaLiga()
            self.primero = x
            return
        x.asignaLiga(y.retornaLiga())
        y.asignaLiga(x)
        if(y == self.ultimo):
            self.ultimo =x
    

    def desconectar(self,nodoX:node,nodoY:node):
        if nodoY ==None :
            if nodoX.retornaLiga()==None:
                self.ultimo=None               
            self.primero=nodoX.retornaLiga()
            return
        nodoY.asignaLiga(nodoX.retornaLiga())    
        if nodoX== self.ultimo: self.ultimo= nodoY
    
# l = listaEnlazada()
# l.append("y")
# l.append("x")
# l.append("b")
# l.append("a")
# l.display()
# l.erase(3)
# l.display()
