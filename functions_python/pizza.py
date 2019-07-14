def make_pizza(size, *toppings):
    print(f"\nMaking your {size}-inch pizza with the ingredient below: ")

    for index, topping in enumerate(toppings, start=1):
        print(f"{index}. {topping.title()}")