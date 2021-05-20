s = [4, 1, 3, 4, 5]
"""
for i in enumerate(s):
    print(i)
"""
ans = 0
for i in enumerate(s):
    for j in enumerate(s):
        if s[i] == s[j] and i<j:
            ans += 1
        i += 1
    j += 1
print (ans)            

    #print(i)
    #if ()
    #print(f"{i} --> {v} ")
