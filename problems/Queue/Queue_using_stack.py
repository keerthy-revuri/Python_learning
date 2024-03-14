# Implement Queue using stack
# method 1 - push is O(n), pop is O(1)
class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
    def enqueue(self,x):
        #Move all elements from s1 to s2 if len(s1) not 0
        while len(self.s1) != 0:
            self.s2.append(self.s1[-1])
            self.s1.pop()
        #push item to self.s1 if len(s1) is empty
        self.s1.append(x)

        # Push all elements from s2 back to s1
        while len(self.s2) != 0:
            self.s1.append(self.s2[-1])
            self.s2.pop()

    def dequeue(self):
        if len(self.s1) == 0:
            return -1
        x = self.s1[-1]
        self.s1.pop()
        return x

qu = Queue()
qu.enqueue(1)
qu.enqueue(2)
qu.enqueue(3)
print(qu.dequeue())
print(qu.dequeue())
print(qu.dequeue())


# method 2 - pop is O(n), push is O(1)
class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
    def enqueue(self, x):
        self.s1.append(x)
    def dequeue(self):
        #if both lengths of stack s1, s2 are empty return -1
        if len(self.s1) == 0 and len(self.s2) == 0:
            return -1
        # if s2 is empty and s1 has elements
        elif len(self.s1 > 0) and len(self.s2) == 0:
            while self.s1:
                temp = self.s1.pop()
                self.s2.append(temp)
            return self.s1.pop()
        else:
            return self.s2.pop()


qu = Queue()
qu.enqueue(1)
qu.enqueue(2)
qu.enqueue(3)
print(qu.dequeue())
print(qu.dequeue())
print(qu.dequeue())


