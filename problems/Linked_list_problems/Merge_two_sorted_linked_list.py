class Node:
    def __init__(self, data = 0, nxt = None):
        self.data = data
        self.next = nxt
class Linkedlist:
    def __init__(self):
        self.head = None
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def print_list(self, new_head):
        curr = new_head
        while curr:
            print(curr.data)
            curr = curr.next
    def merge_two_sorted(self, l1, l2):
        dummy = Node()
        current = dummy
        while l1 and l2:
            if l1.data < l2.data:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        if l1:
            current.next = l1
        while l2:
            current.next = l2
            l2 = l2.next
            current = current.next

        return dummy.next

llist1 = Linkedlist()
llist1.push(4)
llist1.push(2)
llist1.push(1)
#llist1.print_list()
llist2 = Linkedlist()
llist2.push(4)
llist2.push(3)
llist2.push(1)
#llist2.print_list()
new_head = llist1.merge_two_sorted(llist1.head, llist2.head)
llist1.print_list(new_head)