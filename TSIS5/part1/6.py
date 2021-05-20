f = open("in.txt", "r")
line = []
var = ""
line = f.readlines()
for i in line:
    var += i
print(var)    