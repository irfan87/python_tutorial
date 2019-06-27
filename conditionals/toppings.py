# make this app efficiently

requested_toppings = []

requested_toppings.append('mushrooms')
requested_toppings.append('extra cheese')
requested_toppings.append('pepperoni')
requested_toppings.append('green peppers')
requested_toppings.append('anchovies')

if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping == 'green peppers':
            print("Sorry, green peppers are out of stocks")
        elif requested_topping == 'anchovies':
            print("Sorry, anchovies is out of stocks")
        else:
            print(f"Adding {requested_topping.title()}")

    print("\nYour pizza is ready")
else:
    print("\nAre you ready to make some pizzas todays?")