k = int(input())
m = int(input())
n = int(input())
if (k>=n):
    print(2*m)
elif(k<n and (2*n)%k == 0):
    print(int(((2*n)/k)*m))
elif(k<n and (2*n)%k != 0):
    print (int((((2*n)/k)*m)+m))    