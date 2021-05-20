import math
n = int(input())
#print(math.factorial(n)) 
ans = 1
while n>1:
    ans = ans*n
    n = n - 1
print(ans)      