'''
n = int(input())
nums = list(map(int, input().split()))
ans = 0
for i in nums:
    ans += i
print (ans)  
''' 
n = int(input())
ans = 0
i = 0
while i < n:
    nums= int(input())
    ans += nums 
    i += 1
print(ans)    