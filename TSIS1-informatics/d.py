n = int(input())
h = int(n // 30)
m = int((n - h*30)// 0.5)
print ("It is {0} hours {1} minutes.".format(h, m))