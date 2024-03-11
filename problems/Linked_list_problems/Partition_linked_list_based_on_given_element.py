
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
    def print_list(self, new_head):
        a = new_head
        while a:
            print(a.data)
            a = a.next
    def partition(self, head, x):
        left , equal, right = Node(), Node(), Node()
        ltail , etail, rtail = left, equal, right
        while head:
            if head.data < x:
                ltail.next = head
                ltail = ltail.next
            elif head.data == x:
                etail.next = head
                etail = etail.next
            else:
                rtail.next = head
                rtail = rtail.next
            head = head.next
        ltail.next = equal.next
        etail.next = right.next

        return left.next

llist = Linkedlist()
llist.push(5)
llist.push(4)
llist.push(1)
llist.push(3)
llist.push(2)
llist.push(2)
llist.push(1)
new_head = llist.partition(llist.head, 3)
llist.print_list(new_head)
