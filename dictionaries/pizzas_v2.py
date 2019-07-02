pizza = {
    'crust': 'thick',
    'toppings': [
        'mushrooms',
        'extra cheese'
    ]
}

# sumarize the order
print(f"You have ordered a {pizza['crust']}-crust pizza with the toppings")

for index, pizza_topping in enumerate(pizza['toppings'], start=1):
    print(f"\t{index} - {pizza_topping.title()}")