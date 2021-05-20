a = 5
b = "hello"
#print (a + b) #error
print (f"{a} + {b}")

x = "hello" #global

def myfunc():
    y = "world" #local
    print ("everyone " + x + " " + y)

def myfunc2():
    print ("everyone " + x)

myfunc()
myfunc2()
