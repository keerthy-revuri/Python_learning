#single linked list

class Node:
    def __init__(self, val = 0 , nxt = None):
        self.val = val
        self.next = None
class Linked_list:
    def __init__(self):
        self.head = None

    def push(self,val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def append(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def insert_at_position(self,pos,val):
        new_node = Node(val)
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return
        curr = self.head
        for i in range(pos - 1):
            curr = curr.next
        new_node.next = curr.next
        curr.next = new_node

    def print_list(self):
        a = self.head
        while a:
            print(a.val)
            a = a.next

    def delete_at_begining(self):
        self.head = self.head.next

    def delete_at_end(self):
        prev = self.head
        curr = self.head.next
        while curr.next:
            prev = prev.next
            curr = curr.next
        prev.next = None

    def delete_at_position(self, pos):
        prev = self.head
        curr = self.head.next
        for i in range(pos - 1):
            prev = prev.next
            curr = curr.next
        prev.next = curr.next

llist = Linked_list()
llist.push(2)
llist.push(1)
llist.append(3)
llist.append(4)
llist.append(5)
llist.insert_at_position(2, 6)
llist.print_list()
llist.delete_at_begining()
llist.delete_at_end()
llist.delete_at_position(2)
print("after deletion")
llist.print_list()


