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
    def delete_middle(self):
        slow, fast = self.head, self.head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
            prev.next = slow.next



llist = Linkedlist()
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
llist.print_list()
llist.delete_middle()
print("after delete")
llist.print_list()