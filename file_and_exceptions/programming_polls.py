import os

filename = os.path.abspath("file_and_exceptions/programming_polls.txt")
responses = []

while True:
    response = input("\nWhy do you like programming? ")
    response = responses.append(response)

    cont_polls = input("Would you like to let someone to have the poll? ")

    if cont_polls != 'y' and cont_polls != 'yes':
        print("Thanks for taking the polls")
        break

with open(filename, 'a') as f:
    for response in responses:
        f.write(response + "\n")
    