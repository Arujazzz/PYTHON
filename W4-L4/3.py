import re
text = "The     rain    in     Spain"
x = re.split("in", text)
x = re.split(" ", text)
x = re.split("\s+", text)
#x = re.split("\s+", text, 1)
print (x)