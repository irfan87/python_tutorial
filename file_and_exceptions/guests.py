import os

name = input("Please enter your name: ")

filename = os.path.abspath("file_and_exceptions/guests.txt")

with open(filename, 'w') as f:
    f.write(name.title())