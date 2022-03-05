class doubleNode:
    def __init__(self,data=None):
        self.prev = None
        self.data = data
        self.next = None

class LDL:
    def __init__(self):
        self.head = doubleNode()
    def insert(self,data): #data = x
        new_node=doubleNode(data)
        cur=self.head
        while cur.next != None:
            cur=cur.next
        new_node.prev = cur
        cur.next=new_node
        

    
lista = LDL()
lista.insert("x")
lista.insert("y")