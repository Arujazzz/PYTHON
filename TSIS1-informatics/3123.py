s = input()
s1 = s[s.find("h") : s.rfind("h") + 1]
s = s[:s.find("h")] + s1[::-1] + s[s.rfind("h") + 1:]
print(s)
