f = open("in.txt", "r")
array = []
line = f.readlines()
for i in line:
    array.append(i)
print(array)    