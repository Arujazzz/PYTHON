s = 0
p = 1
while n>0:
    digit = n % 10
    s = s + digit
    p = p * digit
    n = n // 10
return(p - s)