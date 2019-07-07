user_responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("\nWhich vacation would you like to visit this year? ")

    user_responses[name] = response

    user_repeat = input("Take the poll again? (Yes/No) ")

    if user_repeat == 'No' or user_repeat == 'no':
        polling_active = False

print("\nBelow is the vacation list that you would like to visit this year:\n")

for name, user_response in user_responses.items():
    print(f"{name.title()} would like to visit {user_response.title()} this year")