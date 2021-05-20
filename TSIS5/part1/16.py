f = open("in.txt", 'r')
f.close()
if f.closed:
    print("file close")
else:
    print("file not close")    