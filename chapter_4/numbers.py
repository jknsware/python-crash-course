# 4.3
numbers = list(range(1, 21))
for number in numbers:
  print(number)
print("\n")

# 4.4
# millions = list(range(1, 1000000))
# for number in millions:
#   print(number)
# print("\n")


# 4.5
millions = list(range(1, 10000001))
print(min(millions))
print(max(millions))
print(sum(millions))
print("\n")

# 4.6
odds = list(range(1, 20, 2))
for odd in odds:
  print(odd)
print("\n")

# 4.7
threes = list(range(3, 31, 3))
for three in threes:
  print(three)
print("\n")

# 4.8
cubes = []
for number in range(1, 11):
  cube = number**3
  cubes.append(cube)

for cube in cubes:
  print(cube)
print("\n")

# 4.9
cubes = [number**3 for number in range(1,11)]
for cube in cubes:
  print(cube)
print("\n")

# 4.10
threes = list(range(3, 31, 3))
print(f"The first three numbers in the slice are: {threes[0:3]}")
print(f"The middle three numbers in the slice are: {threes[4:7]}")
print(f"The last three numbers in the slice are: {threes[7:]}")
