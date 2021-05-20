a = []
a.append(0)
for i in range(0, len(gain)):
    element = a[i] + gain[i]
    a.append(element)
    ans = max(a)
print (ans)    
#return ans    

