import re
with open('in.txt', 'r', encoding = 'utf-8') as f:
    text = f.read()
pattern1 = r'ТОО \w+'
pattern2 = r'БИН \d{12}'
pattern3 = r'\d+\.\s(.+)'
pattern4 = r'\d+,000'
pattern5 = r'x\s(\d+,00)'
pattern6 = r'Стоимость\n(\d+\s?\d*,00)'
pattern7 = r'Время:\s\d{2}\.\d{2}\.\d{4}\s\d{2}\:\d{2}\:\d{2}'
pattern8 = r'г\..+'
namecompany = re.findall(pattern1, text)
binnumber = re.findall(pattern2, text)
title = re.findall(pattern3, text)
cout = re.findall(pattern4, text)
inutprice = re.findall(pattern5, text)
totalprice = re.findall(pattern6, text)
data = re.findall(pattern7, text)
address = re.findall(pattern8, text)
print(*namecompany)
print(*binnumber)
for i in range(len(pattern3)):
    print(title[i])
    print(cout[i])
    print(inutprice[i])
    print(totalprice[i])
print(*data)
print(*address)    
