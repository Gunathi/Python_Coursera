import re

with open('file2.txt', 'r') as file:
    data = file.read()
sum = 0
y = re.findall('[0-9]+',data)
for x in y:
    i = int(x)
    sum = sum + i
    
print (y)
print(sum)
