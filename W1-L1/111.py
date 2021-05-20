s = [1,2,3,1,1,3]
ans = 0
i = 0
#j = 1
for i in range(len(s)):
    for j in range(len(s)):
         if (s[i] == s[j] and i<j):
            ans += 1
            i += 1
            j = i + 1
print (ans)         
          