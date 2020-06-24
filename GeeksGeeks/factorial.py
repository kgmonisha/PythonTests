def fact(n):
    if n == 0:
        return 1
    while n > 0:
        return n*fact(n-1)

print(fact(5))