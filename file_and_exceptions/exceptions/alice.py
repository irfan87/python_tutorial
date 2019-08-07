import os

filename = os.path.abspath("file_and_exceptions/exceptions/alice.txt")

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} is not exits, yet.")
else:
    words = contents.split()
    num_words = len(words)

    print(f"The file {filename} has about {num_words} words")