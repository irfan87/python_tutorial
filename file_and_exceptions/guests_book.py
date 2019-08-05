filename = '/Users/nerve2009/Desktop/python_projects/python_crash_course/file_and_exceptions/guests_book.txt'

print("Enter 'q' or 'quit' to finish")
while True:
    name = input("Please enter your name: ")

    if name == 'q' or name == 'quit':
        print("Bye bye")
        break
    else:
        with open(filename, 'a') as f:
            f.write(name.title() + "\n")

        print(f"Hi {name.title()}, your name is in our guests book.")