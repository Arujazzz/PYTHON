import re
n = int(input())
string = [input() for _ in range(n)]
for num in string:
    if bool(re.match (r'[789][\d]{9}$', num)):
        print ("YES")
    else :
        print ("NO")