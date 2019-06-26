# store buffet in tuple
our_foods = ('nasi goreng', 'mee goreng', 'bihun goreng', 'mix grill', 'roti canai')

print("\nBelow is the buffet that we are currently offer:")
for our_food in list(our_foods):
    print(f"- {our_food.title()}")

# our_foods[0] = 'nasi goreng kampung'
# print(our_food[0])

food_changes = ('nasi goreng', 'mee goreng', 'bihun goreng', 'mix grill', 'roti canai', 'nasi goreng ayam', 'mee soto')

print("\nWe have make a few changes of buffet as below:")
for food_change in list(food_changes):
    print(f"- {food_change.title()}")