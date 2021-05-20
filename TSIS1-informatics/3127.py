s = input()
s1 = s[:s.find("h")+1]
s2 = s[s.rfind("h"):]
s3 = s[s.find("h")+1:s.rfind("h")]
s4 = s3.replace("h", "H")
s5 = s1 + s4 +s2
print (s5)
