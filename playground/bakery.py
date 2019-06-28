# create an application for your custormer's bakery
# your customers is the first timer business woman and she needs an application to manage her cupcakes order
# just a simple application is enough

# TODO: make a list of cupcakes ingredients
available_cupcakes = ['red velvet cupcakes', 'oreo cupcakes', 'vanilla cupcakes', 'funfetti cupcakes', 'chocolate cupcakes', 'tiramisu cupcakes']

available_cupcakes.sort()

# TODO: make an order list of cupcakes
customer_cupcakes = available_cupcakes[3:]
customer_cupcakes.append('peanut butter cupcakes')
customer_cupcakes.append('snickers cupcakes')

# TODO: if cupcakes available, we will show the cupcakes as the list
if available_cupcakes:
    print("We have a lot of variety of cupcakes as below:")
    for available_cupcake in available_cupcakes:
        print(available_cupcake.title())
    
    # TODO: show the list of your customer's cupcake list
    print("\nCustomers ordered: ")
    for customer_cupcake in customer_cupcakes:
        if customer_cupcake in available_cupcakes:
            print(f"{customer_cupcake.title()} - available")
        else:
            # TODO: show the notification if the ordered cupcakes is not available
            print(f"{customer_cupcake.title()} - unavailable.")

    print("\nHot cupcakes is ready to serve.")
else:
    print("Your list of cupcakes are empty. Create one!")