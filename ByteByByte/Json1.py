import json

#json string - read (loads)
p = '{"name": "Bob", "languages": ["Python", "Java"]}'
person = json.loads(p)
print(person)
print(person['name'])

#read a json file (load)
with open("person.json") as f:
    personfile = json.load(f)

print(personfile)
print(personfile["name"])

#convert a dict to json:

person_dict = {'name': 'Monisha', 'age': 12, 'children': 2 }

persondict = json.loads(json.dumps(person_dict))
print(persondict)

