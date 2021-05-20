line = input()
newline =''.join(reversed(line))
if line == newline:
    print("YES")
else:
    print("NO")    