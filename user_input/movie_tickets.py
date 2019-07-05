user_input = "Welcome to Irfan Cinema"
user_input += "\nEnter 'quit' if you want to exit this application\n"
user_input += "\nPlease enter your age: "

while True:
    user_age = input(user_input)

    if user_age == 'quit':
        print("Bye bye..")
        break

    user_age = int(user_age)
        
    if user_age < 3:
        print(f"\nYou are {user_age} years-old and get free movie ticket\n")
    elif user_age < 12:
        print(f"\nYou are {user_age} year-old and have to pay $10 for the movie ticket\n")
    else:
        print(f"\nYou are {user_age} year-old and have to pay $15 for the movie ticket\n")