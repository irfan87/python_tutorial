user_input = "Test three exits with while loop"
user_input += "\nEnter 'quit' or 'q' to exit the application\n"

# exit number 1
# message = ""

# while message != 'quit':
#     message = input(user_input)
#     print(message)

# exit number 2
# active = True

# while active:
#     message = input(user_input)

#     if message == 'quit':
#         active = False
#     else:
#         print(message)

# exit number 3
while True:
    message = input(user_input)

    if message == 'quit' or message == 'q':
        break
    else:
        print(message)