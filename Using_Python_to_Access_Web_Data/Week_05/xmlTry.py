import xml.etree.ElementTree as ET

#First Example
data = '''<person>
    <name> Hansani </name>
    <phone type = "int1"> +94702876596 </phone>
    <email hide = "yes"/>   
</person>'''

tree = ET.fromstring(data)
print("Name: ",tree.find('name').text)
print("Attr: ",tree.find('email').get("hide"))

#Second Example
input = '''<stuff>
    <users>
        <user x = "2">
            <id>001</id>
            <name> Chuck </name>
        </user>
        <user x = "7">
            <id>009</id>
            <name> Hansani </name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input)
userList = stuff.findall('users/user')
print('User count: ',len(userList))
for item in userList:
    print('Name: ',item.find('name').text)
    print('ID: ',item.find('id').text)
    print('Attribute: ',item.get('x'))
