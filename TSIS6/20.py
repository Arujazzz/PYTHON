def fun():
    x = 1
    y = 2
    string = "w3resource" 
print(fun.__code__.co_nlocals)

print("-"*20)

def fun1():
    n = int(input())
    while n>1:
        nums = input()
print(fun1.__code__.co_nlocals)        