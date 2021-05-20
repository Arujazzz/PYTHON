"""
a = input().split()
b = input().split()
a = set(a)
b = set(b)
print(*sorted(set(a).intersection(b)))
"""

print(*sorted(set(input().split()) & set(input().split()), key=int))