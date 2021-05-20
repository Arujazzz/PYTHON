f = open("in.txt", "r")
text = f.read().split()
ans = len(max(text, key = len))
for word in text:
    if len(word) == ans:
        print(word)