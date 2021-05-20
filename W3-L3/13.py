import mymodule
mymodule.f1("Aruzhan")

print('-'*25)

import mymodule
a = mymodule.person1["age"]
b = mymodule.person1["country"]
print(a)
print(b)

print('-'*25)

import mymodule
from mymodule import hello2
hello2()
print ('*'*10)
from mymodule import hello1 as hi 
hi()

print('-'*25)

print(mymodule.x)
