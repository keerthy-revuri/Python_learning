class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        popped_node = self.head
        self.head = self.head.next
        popped_node.next = None
        return popped_node.data
    def peek(self):
        if self.isEmpty():
            return "stack is empty"
        else:
            return self.head.data

    def display(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next

st = Stack()
st.push(1)
st.push(2)
st.push(3)
st.push(4)
st.peek()
st.display()
print(st.pop())
print(st.pop())
print(st.pop())
print(st.pop())

