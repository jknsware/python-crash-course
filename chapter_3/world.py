places = ['seattle', 'new orleans', 'washington', 'orlando', 'nashville']
print("Original order:")
print(places)

print("\nAlphabetical:")
print(sorted(places))

print("\nReverse Alphabetical:")
print(sorted(places, reverse=True))

print("\nOriginal:")
print(places)

print("\nReversed:")
places.reverse()
print(places)

print("\nReverse Again:")
places.reverse()
print(places)

print("\nSorted Alpha:")
places.sort()
print(places)

print("\nReverse Alpha:")
places.sort(reverse=True)
print(places)
