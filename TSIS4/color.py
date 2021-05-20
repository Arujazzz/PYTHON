import re
n = int(input())
check = False
for _ in range(n):
    string = input()
    for j in string.split():
        if j == "{":
            check = True
            continue
        elif j == "}":
            check = False 
            continue
        elif check:
            result = re.search(r'\#[0-9a-fA-F]{3,6}', j)
            if result:
                print(result.group(0))