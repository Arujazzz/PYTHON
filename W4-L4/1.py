import re
text = "The rain in Spain"
x = re.search("^The.*Spain$", text)
x = re.search("in", text)
print(x.start()) #первый индекс
print(x.endpos)  
print(x.span())
print(x.group())