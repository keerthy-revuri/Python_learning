class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Linked_list:
    def __init__(self):
        self.head = None
    def append(self, num):
        new_node = Node(num)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def push(self,num):
        new_node = Node(num)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self,prev_node,num):
        if prev_node is None:
            print("The given prev_node must be in linked list ")
            return
        new_Node = Node(num)
        new_Node.next = prev_node.next
        prev_node.next = new_Node

    def delete_begining(self):
        temp = self.head
        self.head = self.head.next
        temp = None

    def delete_end(self):
        temp = self.head.next
        prev = self.head
        while temp.next:
            temp = temp.next
            prev = prev.next
        prev.next = None

    def delete_specified_pos(self,pos):
        temp = self.head.next
        prev = self.head
        for i in range(1, pos-1):
            temp = temp.next
            prev = prev.next
        prev.next = temp.next
        temp.next = None
    def printlist(self):
        a = self.head
        while a:
            print(a.data)
            a = a.next

llist = Linked_list()
llist.append(6)
llist.push(7)
llist.push(1)
llist.append(4)
llist.insertAfter(llist.head.next, 8)
llist.delete_begining()
llist.delete_end()
llist.delete_specified_pos(2)
llist.printlist()