import re
n = int(input())
for i in range(n):
    name, email = input().split()
    pattern = r"^<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>$"
    if re.match(pattern, email):
        print(name, email)