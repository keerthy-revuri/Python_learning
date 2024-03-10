#Stack can be implemented in 3 ways - using list, using collections_deque, using queue.LifoQueue

#Using List

stack = []
stack.append('a')
stack.append('b')
stack.append('c')
print(f"Initial stack - {stack}")
print("Elements popped - ")
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(f"Final stack - {stack}")

#Using collections.deque

from collections import deque # importing deque class from collections class
stack = deque() # creating an object named as stack for deque class
stack.append('a')
stack.append('b')
stack.append('c')
print(f"Initial stack - {stack}")
print("Elements popped -")
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(f"Final stack - {stack}")


# using queue.LifoQueue
#Queue module also has a LIFO Queue, which is basically a Stack.
# Data is inserted into Queue using the put() function and get() takes data out from the Queue.

from queue import LifoQueue
stack = LifoQueue(maxsize = 3)
print(stack.qsize())
stack.put('a')
stack.put('b')
stack.put('c')
print("Full size",stack.full())
print("stack size",stack.qsize())
print("Elements popped -")
print(stack.get())
print(stack.get())
print(stack.get())
print("empty stack",stack.empty())

