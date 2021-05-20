class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def show(self):
        print(f'{self.firstname} -> {self.lastname}')

p = Person("Aruzhan", "Kubayeva")
p.show()
print('-'*50)

class Student(Person):
    def __init__(self, fname, lname, age, gpa):
        super().__init__(fname, lname)
        self.age = age
        self.gpa = gpa
    def show(self):
        super().show()
        print(self.gpa, self.age)    
p = Student("Aruzhan", "Kubayeva", "18", "3.37")
p.show()