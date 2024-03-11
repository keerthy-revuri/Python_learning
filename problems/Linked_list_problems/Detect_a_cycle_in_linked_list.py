# Detect a cycle in linked list

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
    def print_list(self):
        a = self.head
        while a :
            print(a.data)
            a = a.next
    def cycle(self, pos):
        if pos < 0:
            print("invalid position")
            return
        last = self.head
        while last.next:
            last =last.next

        prev = self.head
        for i in range(pos):
            prev = prev.next
        last.next = prev
    # appending addresses of node to array and check if any address repeats
    # if it does, then cycle exists , otherwise return false

    # def if_cycle_exists(self):
    #     arr = []
    #     curr = self.head
    #     while curr:
    #         if curr not in arr:
    #             arr.append(curr)
    #         else:
    #             print(f"arr - {arr}")
    #             print(f"curr - {curr}")
    #             return True
    #         curr = curr.next
    #
    #     return False


# using slow, fast pointers - if cycle exists at a point slow and fast pointers become equal
    def  if_cycle_exists(self, head):
        slow, fast = head, head
        while fast and fast.next:
             slow = slow.next
             fast = fast.next.next
             if slow == fast:
                return True
        return False

llist = Linkedlist()
llist.push(-4)
llist.push(0)
llist.push(2)
llist.push(3)
#llist.print_list()
pos = 1
llist.cycle(pos)
#llist.print_list()
print(llist.if_cycle_exists(llist.head))
