favorite_places = ['Liverpool', 'Hawaii', 'Singapore', 'Amsterdam', 'Penang', 'Johor']

# original lists
print("\nOriginal List\n")
print(favorite_places)

# original place lists in alphabetical order
print("\nSorted List\n")
print(sorted(favorite_places))

# show again the original lists
print("\nOriginal List\n")
print(favorite_places)

# sorted list as reverse
print("\nReverse List\n")
print(sorted(favorite_places, reverse=True))

# show again the original lists
print("\nOriginal List\n")
print(favorite_places)

# reverse list
print("\nRerverse List\n")
favorite_places.reverse()
print(favorite_places)

# revert to the original place
print("\nOriginal List\n")
favorite_places.reverse()
print(favorite_places)

# sorting the list with sort()
print("\nSorting List")
favorite_places.sort()
print(favorite_places)

# sorting the list in reverse
print("\nSorted list alphabetical\n")
favorite_places.sort(reverse=True)
print(favorite_places)