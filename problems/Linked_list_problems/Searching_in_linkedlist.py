# searching in linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Linked_list():
    def __init__(self):
        self.head = None
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    def print_list(self):
        a = self.head
        while a:
            print(a.data)
            a = a.next

    def search(self,x):
        curr = self.head
        print(f"curr - {curr.data}")
        while curr:
            print(f"curr - {curr.data}")
            if curr.data == x:
                print(f" curr.val - {curr.data}, x = {x}")
                return True
            curr = curr.next
        return False


llist = Linked_list()
llist.push(2)
llist.push(1)
llist.push(3)
llist.append(4)
llist.append(5)
llist.print_list()

if llist.search(4):
    print("element found")
else:
    print("element not found")

