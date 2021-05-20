#print ("Enter any words")

a = input ("Enter any words with letter l: ")
cnt = 0
for i in a:
    if i == "l":
        cnt += 1
print (cnt)