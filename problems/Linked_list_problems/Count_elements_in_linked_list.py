class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def print_list(self):
        a = self.head
        while a:
            print(a.data)
            a = a.next
    def count(self):
        counter = 0
        curr = self.head
        while curr:
            counter = counter + 1
            curr = curr.next
        return counter

llist = Linkedlist()
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
llist.print_list()
print(f"count of elements is - {llist.count()}")