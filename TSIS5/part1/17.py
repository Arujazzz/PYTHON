f = open("in.txt", 'r')
line = f.readlines()
line = [i.strip() for i in line]
print(line)