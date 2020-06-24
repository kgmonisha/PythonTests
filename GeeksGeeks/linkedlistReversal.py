class Node:
    def __init__(self, val=None):
        self.val = val
        self.nextnode = None

    def reverse(self,head):
        curr = head
        previous = nextnode = None
        while curr:
            nextnode = curr.nextnode
            curr.nextnode = previous
            previous = curr
            curr = nextnode

a = Node(1)
b = Node(2)
c = Node(3)
a.nextnode = b
b.nextnode = c

print(c.val)
a.reverse(a)
print(c.nextnode.val)
print(b.nextnode.val)
