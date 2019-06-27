# make this app efficiently

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = []

requested_toppings.append('mushrooms')
requested_toppings.append('extra cheese')
requested_toppings.append('french fries')

if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping in available_toppings:
            print(f"Adding {requested_topping.title()}")
        elif requested_topping == 'green peppers':
            print("Sorry, green peppers are out of stocks")
        elif requested_topping == 'anchovies':
            print("Sorry, anchovies is out of stocks")
        else:
            print(f"Sorry, we don't have {requested_topping.title()}")

    print("\nYour pizza is ready")
else:
    print("\nAre you ready to make some pizzas todays?")