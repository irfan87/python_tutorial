# define my favorite pizzas and my friend's favorite pizzas
my_fav_pizzas = ['blazing seafood', 'chicken supreme', 'hawaiian supreme']
my_friend_fav_pizzas = my_fav_pizzas[:]

# append both our favorite pizzas
my_fav_pizzas.append('super supereme')
my_fav_pizzas.append('tripple chicken')

my_friend_fav_pizzas.append('aloha chicken')
my_friend_fav_pizzas.append('beef pepperoni')

# sort out our favorite pizzas
my_fav_pizzas.sort()
my_friend_fav_pizzas.sort()

# show our both favorite pizzas in to separate list
print("My Favorite Pizzas:")
for my_fav_pizza in list(my_fav_pizzas):
    print(my_fav_pizza.title())

print("\nMy Friend's Favorite Pizzas:")
for my_friend_fav_pizza in list(my_friend_fav_pizzas):
    print(my_friend_fav_pizza.title())