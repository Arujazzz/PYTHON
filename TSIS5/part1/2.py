n = int(input())
with open("in.txt", "r") as f:
    #text = f.readline()
    for i in range(n):
        text = f.readline()
        print(text, end = "")