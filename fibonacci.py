import time

def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a
res = fib(12)
print(res)


