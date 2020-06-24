class stack():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self,x):
        self.items.append(x)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if len(self.items) > 0:
            return self.items[-1]

    def size(self):
        return len(self.items)

s1 = stack()
print(s1.isEmpty())
s1.push(2)
s1.push(3)
print(s1)
print(s1.pop())
print(s1.peek())
print(s1.size())