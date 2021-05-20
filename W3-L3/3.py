x = lambda a:a+10
print(x(10))
print('-'*50)

x = lambda a, b:a+b
print(x(5, 5))
print('-'*50)

def f1(n):
    return lambda x:x*n
mydoubler = f1(2)
mytripler = f1(3)
print(mydoubler(11))
print(mytripler(11))     
print('-'*50)

