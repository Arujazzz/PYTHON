def isprime():
    n = int(input())
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            return ("number is not prime")
    return ("number is prime")
print(isprime())     