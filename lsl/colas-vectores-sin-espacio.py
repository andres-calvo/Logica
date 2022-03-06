class CircularQueue(object):
    """
         Cola circular
    """
    MAX_QUEUE_SIZE = 6

    def __init__(self):
        self.data = [None for _ in range(CircularQueue.MAX_QUEUE_SIZE)]  # Simular matriz de tamaño fijo
        self.front, self.rear = 0, 0

    def enter_queue(self, x):
        if self.is_full():
            raise Exception("queue is full.")
        self.data[self.rear] = x
        self.rear = (self.rear + 1) % CircularQueue.MAX_QUEUE_SIZE
        return True

    def del_queue(self):
        if self.is_empty():
            return None
        val = self.data[self.front]
        self.front = (self.front + 1) % CircularQueue.MAX_QUEUE_SIZE
        return val

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return (self.rear + 1) % CircularQueue.MAX_QUEUE_SIZE == self.front  # Sacrifica una unidad para distinguir entre lleno y vacío

    def size(self):
        return (self.rear - self.front + CircularQueue.MAX_QUEUE_SIZE) % CircularQueue.MAX_QUEUE_SIZE

    def get_front(self):
        if not self.is_empty():
            return self.data[self.front]
        else:
            return None

    def clear(self):
        self.__init__()

    def __str__(self):
        ret_str = "queue["
        start, end = self.front, self.rear
        while start != end:
            ret_str += str(self.data[start]) + ", "
            start = (start + 1) % CircularQueue.MAX_QUEUE_SIZE
        ret_str += "]"
        return ret_str

    def __repr__(self):
        return self.__str__()
 
cola=CircularQueue ()
cola.enter_queue(1)
cola.enter_queue(5)
cola.enter_queue(7)
cola.del_queue()
cola.enter_queue(7)
print(cola)