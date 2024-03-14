class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.front = self.rear = None
    def is_Empty(self):
        return self.front == None
    def enqueue(self, data):
        temp = Node(data)
        if self.rear == None:
            self.rear = self.front = temp
            return
        self.rear.next = temp
        self.rear = temp
    def dequeue(self):
        if self.is_Empty():   # this function handles the edge case which is when dequeue() function is called on empty queue
            return "Queue is empty"
        val = self.front.data
        self.front = self.front.next
        return val
        if self.front == None: # this handles the edge case which is when all elements are removed , self.front maps to None, then map self.rear to None
            self.rear = None

qu = Queue()
qu.enqueue(1)
qu.enqueue(2)
qu.enqueue(3)
print(qu.dequeue())
print(qu.dequeue())
print(qu.dequeue())


