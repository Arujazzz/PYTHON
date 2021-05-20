import re
pattern = r"^M{0,3} (CM|CD|C?D {0,3}) (XC|XL|X?L{0,3}) (IX|IV|I?V {0,3})$"
print(str(bool(re.match(pattern, input()))))