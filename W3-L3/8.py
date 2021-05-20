'''
class mynum:
    def __iter__(self):
        self.n = 1
        return self
    def __next__(self):
        x = self.n 
        self.n += 1
        return x
myclass = mynum()
myiter = iter(myclass)  
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))     
'''

'''
class mynum:
    def __iter__(self):
        self.n = 1
        return self
    def __next__(self):
        if self.n <= 10:
            x = self.n
            self.n += 1
            return x
        else:
            raise StopIteration    
myclass = mynum()
myiter = iter(myclass)  
#print(next(myiter))
#print(next(myiter))
#print(next(myiter))
#print(next(myiter))
for x in myiter:
    print(x)
'''    

