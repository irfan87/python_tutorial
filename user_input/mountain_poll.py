responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("\nWhich mountain would you like to climb someday? ")

    # store the response in dictionary
    responses[name] = response

    # someone else want to join?
    repeat = input("Would you like to let another person respond? (Yes/No) ")

    if repeat == 'No' or repeat == 'no':
        polling_active = False

# show the result after polling is completed
print("\n---Poll Result---")

for name, response in responses.items():
    print(f"{name.title()} would like to climb {response.title()}")