person = {"name": "Alice", "age": 25, "city": "Hinganghat"}
print(person)
print(person["name"])
print(person["age"])
# use of .get()
print(person.get("height"))
# adding and updating items
person["job"] = "Engineer"
person["age"] = 26
print(person)
# pop(): Removes a key and returns its value
age = person.pop("age")
print(age)
print(person)
# del: Removes a key without returning its value
del person["city"]
print(person)

#looping through a dictionary
#looping through Keys
for key in person:
    print(key)

#looping through values
for value in person.values():
    print(value)

#looping through key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")
