person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

print(person)
print(person['children'][1])


print(person['pets']['cat'])
# print name of children using for loop
for child in person['children']:
    print(child)

#print name of cats using for loops

for pet in person['pets']:
    print (person['pets'][pet])