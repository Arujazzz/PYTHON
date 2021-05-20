a = 10    #global var
def hello():
    x = 2 #local var
    
    def hi():
        print(x)
    hi() 
hello()
print(a)     