s = input()
ans1 = 0
ans2 = 0
for i in s:
    if i.isupper():
        ans1 += 1
    elif i.islower():
        ans2 += 1    
print("of Upper case characters : " , ans1)        
print("of Lower case Characters : " , ans2)