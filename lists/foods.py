my_foods = []

my_foods.append('nasi goreng')
my_foods.append('mix grill')
my_foods.append('lamb chop')

friend_foods = my_foods[:]

friend_foods.append('macdonald')
friend_foods.append('kfc')

print("\nbelow is my favorite foods".title())

for my_favorite_food in list(my_foods):
    print(my_favorite_food.title())

print("\nbelow is my friend's favorite foods".title())
for friend_favorite_food in list(friend_foods):
    print(friend_favorite_food.title())