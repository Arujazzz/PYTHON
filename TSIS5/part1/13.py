with open("13first.txt", "r") as f1, open ("13second.txt", "a") as f2:
    for i in f1:
        f2.write(i)