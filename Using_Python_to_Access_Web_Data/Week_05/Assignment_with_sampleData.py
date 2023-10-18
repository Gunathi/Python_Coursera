import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

fhand = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_42.xml')

data = fhand.read().decode()

tree = ET.fromstring(data)
counts = tree.findall('.//count')
print('Count: ',len(counts))
sum = 0
for item in counts:
    # print('Count: ',item.text)
    sum = sum + (int)(item.text)

print(sum)
