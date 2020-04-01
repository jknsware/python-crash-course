fav_numbers = {
  "paul": ["1", "6"],
  "frank": ["2", "7", "8"],
  "george": ["3", "9", "10"],
  "bob": ["4", "11"],
  "steve": ["5", "12"]
}

for name, numbers in fav_numbers.items():
  print(f"\n{name.title()}'s favorite numbers are:")
  for number in numbers:
    print(f" {number}")
