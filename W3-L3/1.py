def hello():
    print("hello pp2")
hello()  
print("-"*50)

def square(a):
    print(a*a)
square(2)
print("-"*50)

def sum(a, b):
    print(a+b)
sum(2, 4)
print("-"*50)  

def f1(*args):
    for i in args:
        print(i)
f1(1, "pp2", {'code': 123}, False)
print("-"*50)  

def f2(a, b, *args):
    print(a, b)
    for i in args:
        print(i)
f2(2, 4, "pp2", {'code': 123}, False, 2.4)
print("-"*50)     

def f3(name, age):
    print(f"{name} -> {age}")
#f3(name = "Aruzhan", age = "18")
f3("Aruzhan", "18") 
print("-"*50)

def f4(name, age, **kwargs):
    print(f'{name} -> {age}')
    for i in kwargs:
        print(f'{i} -> {kwargs[i]}')
f4(name = "Aruzhan", age = "18", gpa = "3.37", year = "1", faculty = "FIT")
print("-"*50) 

def f5(nums):
    for i in nums:
        print(i*2)
f5([2, 4, 6, 8, 10])        
