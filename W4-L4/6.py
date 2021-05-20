import re
with open("in.txt", "r") as f:
    text = f.read()
pattern1 = r'\w+stan'
ans1 = re.findall(pattern1, text)
print(ans1)
print('-'*20)

with open("in.txt", "r") as f:
    text = f.read()
pattern2 = r'\d{2}\.\d{2}\.\d{2,4}'
ans2 = re.findall(pattern2, text)
print(ans2)
print('-'*20)

with open ("in.txt", "r") as f:
    text = f.read()
pattern3 = r'\d{2}\:\d{2}\:\d{2}'
ans3 = re.findall(pattern3, text)
print(ans3)
print('-'*20)

'''
with open ("in.txt", "r") as f:
    text = f.read()
#pattern4 = '(\+7|8)\(?\d{3}\)?-?\d{3}-\d{2}-\d{2}'
print(re.findall('(\+7|8)\(?\d{3}\)?-?\d{3}-\d{2}-\d{2}', text))
#print(ans4)
'''
with open ("in.txt", "r") as f:
    text = f.read()
#pattern4 = r'[A-Za-z0-9_]+\.?[A-Za-z0-9_]+@[a-z]+\.[a-z]{2,4}'
pattern4 = r'[\w]+\.?[\w]+@[\w]+\.[\w]{2,4}'
ans4 = re.findall(pattern4, text)
print(ans4)
print('-'*20)

with open ("in.txt", "r") as f:
    text = f.read()
pattern5 = r'[\w+\]'
ans5 = re.findall(pattern5, text)
#print(ans5)    