favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, language in favorite_languages.items():
  print(f"{name.title()}'s favorite language is {language.title()}.")

print("\n")

coders = ['phil', 'sydney', 'david', 'natalie', 'sarah', 'jason', 'kelli']
for name in coders:
  if name in favorite_languages.keys():
    print(f"Thank you for taking the poll, {name.title()}.")
  else:
    print(f"{name.title()}, what's your favorite language?")
