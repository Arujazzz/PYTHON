import random
with open("in.txt", "r") as f:
    line = f.readlines()
    print(random.choice(line))
