s = list(map(int, input().split()))
nset = set()
for i in s:
    print('YES') if i in nset else print('NO')
    nset.add(i)