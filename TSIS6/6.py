n = int(input())
a, b = [i for i in input().split()]
a = int(a)
b = int(b)
if n in range(a, b):
    print("this number in range")
else:
    print("not found")