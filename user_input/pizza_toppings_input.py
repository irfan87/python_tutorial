user_message = "Welcome to the Irfan Pizza"
user_message += "\nEnter 'quit' when you have done to make the order\n"

while True:
    toppings = input(user_message)

    if toppings == 'quit':
        print("\nUntil we meet again..")
        break
    else:
        print(f"\nI want {toppings} on my pizza\n")