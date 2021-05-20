n = int(input())
a = {}
for i in range(n):
    s, t = input().split()
    a[s] = t
    a[t] = s
b = input()    
print(a[b])

