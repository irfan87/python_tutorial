from name_function import get_formatted_name

print("Enter 'quit', 'q', 'Quit', or 'Q' to exit")

while True:
    user_first_name_input = input("\nPlease enter your first name: ")
    user_prompt_answer = ['q', 'quit', 'Quit', 'Q']

    if user_first_name_input in user_prompt_answer:
        print("Bye bye")

        break
    
    user_last_name_input = input("\nPlease enter your last name: ")

    if user_last_name_input in user_prompt_answer:
        print("Bye bye")

        break

    formatted_name = get_formatted_name(user_first_name_input, user_last_name_input)
    print(f"\nYour fullname is {formatted_name}")