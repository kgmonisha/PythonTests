def fibonacci(n):
    a = 0
    b = 1
    if n == 1:
        return 0
    if n == 2:
        return 1
    for i in range(3,n+1):
        c = a + b
        a = b
        b = c
    return c
print(fibonacci(5))

def fibonaccirecur(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonaccirecur(n-1) + fibonaccirecur(n-2)

print(fibonaccirecur(5))