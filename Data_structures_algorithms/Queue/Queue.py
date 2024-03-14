# Using List

queue = []
queue.insert(0,'a')
queue.insert(0,'b')
queue.insert(0,'c')
print(f"after insertion-{queue}")

print(f"first popped element is - {queue.pop()}")
print(f"second popped element is - {queue.pop()}")

# Using Collections.deque

from collections import deque
queue = deque()
queue.insert(0, 'e')
queue.insert(0,'f')
queue.insert(0,'g')
queue.appendleft('h')
print(f"after insertion - {queue}")

print(f"first popped element is - {queue.pop()}")


#Using Queue Class

from collections import deque
class Queue:
    def __init__(self):
        self.buffer = deque() # ctrl + B - to view methods in deque class (appendLeft is a method , buffer is a obeject here)
    def enqueue(self, val):
        self.buffer.appendleft('apple')
        self.buffer.appendleft("banana")
    def dequeue(self):
        return self.buffer.pop()
    def isEmpty(self):
        return len(self.buffer)
    def size(self):
        return 





