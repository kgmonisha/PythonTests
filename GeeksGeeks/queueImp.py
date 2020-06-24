class queue():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self,x):
        self.items.append(x)

    def dequeue(self):
        item = self.items[0]
        self.items = self.items[1:]
        return item

    def size(self):
        return len(self.items)

s1 = queue()
print(s1.isEmpty())
s1.enqueue(2)
s1.enqueue(3)
print(s1)
print("deuque")
print(s1.dequeue())
print(s1.size())