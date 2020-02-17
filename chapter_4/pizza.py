# 4.1
pizzas = ['pepperoni', 'hawaiian', 'cheese']
for pizza in pizzas:
  print(pizza)
print()

for pizza in pizzas:
  print(f"I like {pizza} pizza.")

print("I really like pizza.")
print("\n")

# 4.2
animals = ['dog', 'cat', 'monkey']
for animal in animals:
  print(f"A {animal} would make a really good pet.")
print(f"These would make great pets.")
print("\n")

# 4.11
pizzas = ['pepperoni', 'hawaiian', 'cheese']
friend_pizzas = pizzas[:]
pizzas.append("meat lover's")

print(f"My favorite pizzas are:")
for pizza in pizzas:
  print(pizza)
print()

print(f"My friend's favorite pizzas are:")
for pizza in friend_pizzas:
  print(pizza)
print("\n")

# 4.12
foods = ["pizza", "falafel", "carrot cake", "cannoli"]
friends_foods = ["pizza", "falafel", "carrot cake", "ice cream"]

print(f"My favorite foods are:")
for food in foods:
  print(f" - {food}")
print()

print("My friend's favorite foods are:")
for food in friends_foods:
  print(f" - {food}")
print("\n")

# 4.13
buffet = ("burgers", "fries", "hot dog", "shakes", "apple pie")
for food in buffet:
  print(food)
# buffet[0] = "pizza"
print()
buffet = ("pizza", "tots", "hot dog", "shakes", "apple pie")
for food in buffet:
  print(food)
