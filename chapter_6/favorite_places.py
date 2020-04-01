favorite_places = {
  'jason': ['enchanted rock', 'mckinney falls'],
  'natalie': ['red rocks', 'galveston'],
  'sydney': ['the park', 'galveston']
}

for name, places in favorite_places.items():
  print(f"\n{name.title()} likes the following places:")
  for place in places:
    print(f"- {place.title()}")
