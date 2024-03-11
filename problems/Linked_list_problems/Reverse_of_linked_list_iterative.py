# Reverse a single linked list

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
    def reverse(self):
        prev =  None
        curr = self.head
        while curr :
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

llist = Linkedlist()
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
llist.print_list()
llist.reverse()
print("after reverse")
llist.print_list()
