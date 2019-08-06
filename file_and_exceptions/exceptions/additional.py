print("Enter 'q' or 'quit' to exit")

while True:
    try:
        number_one = input("\nPlease enter your first number: ")

        if number_one == 'q' or number_one == 'quit':
            break

        number_one = int(number_one)

        number_two = input("\nPlease enter your second number: ")

        if number_two == 'q' or number_two == 'quit':
            break

        number_two = int(number_two)
    except ValueError:
        print("\nOnly integer is allowed")
    else:
        result = number_one + number_two

        print(f"\nThe sum between {str(number_one)} and {str(number_two)} is {str(result)}") 