from datetime import datetime
a = datetime.now()
print(a.year)
print(a.month)
print(a.day)
print(a.hour)
print(a.minute)
print(a.second)
print(a.microsecond)

print('-'*25)

b = datetime(2021, 2, 25, 21, 41, 0)
print(b)

print('-'*25)

print(a.strftime('%d/%m/%Y %H:%M:%S'))