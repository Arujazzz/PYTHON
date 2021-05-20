a = set(input().split())
b = set(input().split())

print(*sorted(set(input().split()) & set(input().split()), key=int))
