s = input()
s1 = s[s.find("h") + 1:]
s2 = s[:s.rfind("h") ]
s3 = s2 + s1
print(s3)


