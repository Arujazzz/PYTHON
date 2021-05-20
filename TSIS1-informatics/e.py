k, n = map(int, input().split())
page=((n - 1) // k) + 1
line=((n - 1) % k) + 1 
print(page, line)

"""
k   n
20 25

2 5
p l
"""