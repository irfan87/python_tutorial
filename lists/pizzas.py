favorite_pizzas = ['blazing seafood', 'chicken supreme', 'hawaiian supreme', 'island supreme']

favorite_pizzas.sort(reverse=True)
favorite_pizzas_size = len(favorite_pizzas)

for favorite_pizza in favorite_pizzas:
    print(favorite_pizza)

print('\n')

for favorite_pizza in favorite_pizzas:
    favorite_pizza_message = f"I like {favorite_pizza} so much."
    print(favorite_pizza_message)

print("\nI love pizzas!!!")
print(f"I love {favorite_pizzas_size} pizzas so much!!")