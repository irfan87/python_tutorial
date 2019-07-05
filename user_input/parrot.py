parrot_msg = "\nTell me something and I will repeat it again to you.."
parrot_msg += "\nEnter 'quit' to end the program "

active = True

while active:
    message = input(parrot_msg)

    if message != 'quit':
        print(f"\n{message}")
    else:
        active = False
        print("Bye bye..")