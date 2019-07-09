def get_formatted_name(first_name, last_name, middle_name=''):

    if middle_name:
        fullname = f"{first_name} {middle_name} {last_name}"
    else:
        fullname = f"{first_name} {last_name}"

    return fullname.title()

# musician = get_formatted_name('john', 'lee', 'hooker')
# print(musician)

# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)

while True:
    print("\nPlease tell me your name: ")
    print("Press 'q', or type 'quit' or 'Quit' to exit the program")

    first_name = input("First Name: ")

    if first_name == 'quit' or first_name == 'q' or first_name == 'Quit':
        break

    last_name = input("Last Name: ")

    if first_name == 'quit' or first_name == 'q' or first_name == 'Quit':
        break

    formatted_name = get_formatted_name(first_name, last_name)

    print(f"\nHello {formatted_name}")