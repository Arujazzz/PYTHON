def myfun(s):
    def add(t):
        nonlocal s
        return s + t
    return add
test = myfun("Hello ")
print(test("World"))    
print("-"*20)
def myfun1(a):
    def add1(b):
        return a + b
    return add1
test1 = myfun1(4) 
print(test1(4))       