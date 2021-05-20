class Person:
    def __init__(self, n, a):
        self.name = n
        self.age = a
#p = Person('Aruzhan', '18') 
#print(p.name, p.age) 
    def show(self):
        print(f'{self.name} -> {self.age}')
p = Person('Aruzhan', '18') 
p.show()        