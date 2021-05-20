import json
a = '{"name": "Aruzhan", "age": 18, "city": "Uralsk"}'
b = json.loads(a)
print(type(a))
print(type(b))
print(b["name"])
print(b["age"])
print(b["city"])

print('-'*25)

c = json.dumps(a)
print(type(c))
print(c)

print('-'*25)