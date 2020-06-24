class Node:
    def __init__(self, val=None):
        self.val = val
        self.nextnode = None

    def nthToLast(self,head,n):
        sec = first = head

        while n:
            sec = sec.nextnode
            n -= 1

        while sec:
            first = first.nextnode
            sec = sec.nextnode

        return first.val



a = Node(1)
b = Node(2)
c = Node(3)
a.nextnode = b
b.nextnode = c

print(c.val)
print(a.nthToLast(a,3))

