people = []

person = {
  'first_name': 'jason',
  'last_name': 'ware',
  'age': '42',
  'city': 'cedar park',
}
people.append(person)

person = {
    'first_name': 'stuart',
    'last_name': 'ware',
    'age': '39',
    'city': 'liberty hill',
}
people.append(person)

person = {
    'first_name': 'chad',
    'last_name': 'ware',
    'age': '37',
    'city': 'euless',
}
people.append(person)

for person in people:
  name = f"{person['first_name'].title()} {person['last_name'].title()}"
  age = person['age']
  city = person['city'].title()

  print(f"{name}, of {city}, is {age} years old.")
