a = input().split()
k = int(input())
b = len(a)
k = k%b
if k<0:
    k = abs(k)
    print(*a[k:],end =' ')
    print(*a[0:k])
    exit()
if k>=0:
    k = abs(k)
    print(*a[-k:],end =' ')
    print(*a[0:-k])
    exit()