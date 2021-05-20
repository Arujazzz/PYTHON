n = int(input())
f = open("in.txt", "r") 
line = f.readlines()
last = line[-n:]
print(*last, end="")