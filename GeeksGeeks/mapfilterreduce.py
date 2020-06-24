from functools import reduce

def square(x):
    return x * x
l1= [1,2,3,4]
op = map(square,l1)
print(list(op))

print(list(map(lambda x: (x%2 != 0),l1)))
print(list(filter(lambda x: (x%2 != 0),l1)))
print(reduce(lambda x,y: x+y, l1))

s = "aBAhdskhas"
print("".join(list(filter(lambda x: x.islower(),s))))


