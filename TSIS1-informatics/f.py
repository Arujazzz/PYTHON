h1, m1, s1 = [int(x) for x in input().split()]
h2, m2, s2 = [int(x) for x in input().split()]
print((h2*3600 + m2*60 + s2) - (h1*3600 + m1*60 + s1))