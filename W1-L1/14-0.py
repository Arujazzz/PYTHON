"""
4
1 2 3 4
"""
n = int (input())
#print (type(n))
nums = input().split()
#print (nums.split())
#print (type(nums[0]))
sum1 = 0
for i in nums:
    if (int(i) % 2 == 0):
        sum1 += int(i)
print (sum1)