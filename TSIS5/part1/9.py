f = open("in.txt", "r")
line = f.readlines()
ans = 0
for i in line:
    ans += 1
print(ans)    