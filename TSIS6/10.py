l = list(map(int, input().split()))
ans1 = ""
for i in l:
    if i%2 == 0:
        ans1 = ans1 + str(i) 
print(list(ans1))  
print("-"*15)      
ans2 = []
for i in l:
    if i%2 == 0:
        ans2.append(i)
print(ans2)         