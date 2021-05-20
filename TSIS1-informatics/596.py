x, y = (int(i) for i in input().split())
n = 1
while x < y:
    x *= 1.7
    n += 1
print(n)