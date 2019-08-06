print("Please enter two numbers")
print("Press 'q' or 'quit' to finish")

while True:
    first_number = input("\nFirst Number: ")
    
    if first_number == 'q' or first_number == 'quit':
        print("Bye bye")
        break

    second_number = input("\nSecond Number: ")

    if second_number == 'q' or second_number == 'quit':
        print("Bye bye")
        break

    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can not divide with 0")
    else:
        print(answer)