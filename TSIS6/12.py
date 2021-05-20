s = input()
t = reversed(s)
t1 = ""
for i in t:
    if i != " ":
        t1 = t1 + i
if t1 == s:
    print("string is palindrom")
else:
    print("string is not palindrom")    