def gen():
    yield 1
    yield 2
    yield 3
it = gen()
print(next(it))  
print(next(it)) 
print(next(it)) 

print('-'*25)

def gen2():
    for i in range(10):
        yield(i)
it = gen2()
#print(next(it)) 
#print(next(it)) 
#print(next(it))   
for i in it:
    print(i)      
