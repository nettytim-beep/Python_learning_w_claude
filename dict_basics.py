person = {"name": "Tim", "age": 40, "city": "Suwanee"}
print(f"person dict {person}")

print(f"person['name'] = {person['name']}")

person["job"] = "Engineer"
print(f"add key/value person['job'] = 'Engineer' dict = {person}")

person["age"] = 41
print(f"update age person['age'] = 41 dict = {person}")

del person["city"]
print(f"delete key/value del person['city']  dict = {person}")

print(f"Does the name key exist in person  'name' in person = {'name' in person}")

print()

print("Loop over keys only")
for key in person:
   print(key)

print()
print("Loop over key/value pairs")
for key, value in person.items():
   print(f"{key}: {value}")

print()
print("Loop over values")
for value in person.values():
   print(value)


