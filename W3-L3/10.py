def fib(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a+b
iter = fib(10)
for i in iter:
    print(i)

print('-'*25)

def fib2(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a+b
iter = fib2(10)
for i in iter:
    print(i)                
