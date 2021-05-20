with open("14first.txt", "r") as f1, open("14second.txt", "r") as f2:
    for l1, l2 in zip(f1, f2):
        print(l1 + l2)