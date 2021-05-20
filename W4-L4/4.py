import re
text = "The            rain    in     Spain"
x = re.sub("in", "**", text)
x = re.sub("\s+", " ", text)
print(x)