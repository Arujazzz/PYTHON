name = ['Aruzhan', 'Gulsezim', 'Sharizda', 'Aigerim', 'Kamilla']
f = open("text.txt","w")
for i in name:
    f.write('%s\n' % i)
text = open("text.txt", "r")
print(text.read())
