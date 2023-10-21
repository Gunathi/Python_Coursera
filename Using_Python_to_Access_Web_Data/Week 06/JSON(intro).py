import json

data = '''{
    "name" : "Hansani",
    "phone" : {
        "type" : "intl",
        "number" : "+94702876596"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads(data)
print('Name: ', info["name"])
print("Hide: ", info["email"]["hide"])

print("")
input = '''[
    { "id" : "001",
      "x" : "2",
      "name" : "Hansani"
    },
    { "id" : "009",
      "x" : "7",
      "name" : "Nimasha"
    }
]'''

info = json.loads(input)
print("User count: ", len(info))

for item in info:
    print("id: ", item["id"])
    print("attr: ", item["x"])
    print("Name: ", item["name"])
