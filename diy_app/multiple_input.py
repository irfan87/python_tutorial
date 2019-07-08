# create a first input
user_input_one = input("\nWhat is your name? ")
user_input_two = input("\nWhat is your age? ")

user_input_two = int(user_input_two)

if user_input_two <= 10:
    print("So young")
elif user_input_two <= 20:
    print("Teen")
elif user_input_two <= 40:
    print("Adult")
else:
    print("Senior")

print(f"\nYour name is {user_input_one.title()} and you are {user_input_two}")
