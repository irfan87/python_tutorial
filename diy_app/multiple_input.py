user_responses = {}

get_user_info = True

while get_user_info:
    user_name = input("\nPlease enter your name: ")
    user_age = input("\nPlease enter your age: ")
    user_age = int(user_age)

    user_responses[user_name] = user_age

    user_repeat = input("\nWant to take this questionaire again? (Yes/No) ")

    if  user_repeat == 'no':
        get_user_info = False

print("\nBelow is your actual data")

for username, user_response in user_responses.items():
    # print(f"\nYour name is {username.title()} and your age is {user_response} years old")
    
    if user_response < 3:
        print(f"{username.title()}, {user_response} is an infant")
    elif user_response <= 12:
        print(f"{username.title()}, {user_response} is a child")
    elif user_response <= 18:
        print(f"{username.title()}, {user_response} is a teenager")
    elif user_response <= 25:
        print(f"{username.title()}, {user_response} is a young adult")
    elif user_response <= 40:
        print(f"{username.title()}, {user_response} is an adult")
    else:
        print(f"{username.title()}, {user_response} is an old person")