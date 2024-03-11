
class Node:
    def __init__(self, data=0, nxt = None):
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
    def remove(self,data):
        if self.head is None:
            return
        while self.head.data == data:
            self.head = self.head.next
        curr = self.head
        #print(f"curr - {curr.data}")
        while curr and curr.next:
            if curr.next.data == data:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return self.head


llist = Linkedlist()
llist.push(4)
llist.push(2)
llist.push(3)
llist.push(2)
llist.push(2)
llist.push(2)
#llist.print_list()
new_head = llist.remove(2)
llist.print_list(new_head)


#---------------------------------
# using dummy node
print("using dummy node")
class Node:
    def __init__(self, data=0, nxt = None):
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
    def remove(self,data):
        dummy = Node(nxt = self.head)
        prev, curr = dummy, self.head
        while curr:
            if curr.data == data:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return dummy.next


llist = Linkedlist()
llist.push(4)
llist.push(2)
llist.push(3)
llist.push(2)
llist.push(2)
llist.push(2)
#llist.print_list()
new_head = llist.remove(2)
llist.print_list(new_head)
