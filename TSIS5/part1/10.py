import os 
from collections import Counter
f = open('in.txt', "r")
text = f.read()
text.replace(':', '')
text = text.split()
print(Counter(text))