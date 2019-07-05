prompt_message = "Please enter which city do you like to visit: "
prompt_message += "\nEnter 'quit' to exit this program\n"

while True:
    city = input(prompt_message)

    if city == 'quit':
        break
    else:
        print(f"I like to visit {city.title()}\n")