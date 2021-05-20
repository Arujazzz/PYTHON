s = input()
size = len(s)
t = ""
for i in range(size):
    if (i%3!=0):
        t = t + s[i]        
print (t)
       