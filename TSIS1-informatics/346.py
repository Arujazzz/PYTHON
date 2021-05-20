n = int(input())
ans1 = 0
ans2 = 0
ans3 = 0
i = 0
while i<n:
    nums = int(input())
    if nums == 0:
        ans1 += 1
    elif nums > 0:
        ans2 += 1
    else:
        ans3 += 1
    i += 1    
print(ans1, ans2, ans3)                