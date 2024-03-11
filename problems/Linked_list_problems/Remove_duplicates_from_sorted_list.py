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
    def remove(self):
        curr = self.head
        while curr and curr.next:
            # print(f"curr.next - {curr.next.data}")
            while curr.data == curr.next.data:
                print(f"curr - {curr.data}, curr.next - {curr.next.data}")
                curr.next = curr.next.next
                print(f"curr - {curr.data}, curr.next - {curr.next}")
            curr = curr.next
        return self.head


    def print_list(self, res):
        curr = res
        while curr:
            print(curr.data)
            curr = curr.next
llist = Linkedlist()
llist.push(2)
llist.push(1)
llist.push(1)
llist.push(1)
#llist.print_list()
res = llist.remove()
print("after remove")
llist.print_list(res)
