n = int(input())
sum1 = 0
sum2 = 0
for i in range(1, n):
    if n%i == 0:
        sum1 += i
for i in range(1, n+1):
    if n%i == 0:
        sum2 += i
if n == sum1 and sum2/2 == n:
    print("number is perfect")                
else:
    print("number is not perfect")