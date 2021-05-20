"""
a = [3, 1, 4]
b = a
b.append(5)
print (a)
print (b)
"""
a = [3, 1, 4]
b  = a.copy()
a.append(6)
b.append(5)
print(a)
print(b)