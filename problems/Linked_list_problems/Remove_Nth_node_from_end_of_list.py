class Node:
    def __init__(self, data = 0, nxt = None):
        self.data = data
        self.next = nxt
class Linkedlist:
    def __init__(self):
        self.head = None
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def remove_Nth_node_from_end(self, n):
        counter = 0
        curr = self.head
        while curr:
            counter = counter + 1
            curr = curr.next
        #print(counter)
        prev = Node(nxt = self.head)
        curr1 = self.head
        #print(f"prev - {prev.data}, curr1 - {curr1.data}")
        for i in range(counter-n):
            prev = prev.next
            curr1 = curr1.next
        prev.next = curr1.next

        return self.head

    def print_list(self, new_head):
        curr = new_head
        while curr:
            print(curr.data)
            curr = curr.next

llist = Linkedlist()
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
#llist.print_list()
n = 2
new_head = llist.remove_Nth_node_from_end(n)
llist.print_list(new_head)