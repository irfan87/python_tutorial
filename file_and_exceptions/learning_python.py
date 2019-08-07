import os

filename = os.path.abspath("file_and_exceptions/learning_python.txt")

print("Reading the file")
with open(filename) as file_objects:
    contents = file_objects.read()
    
print(contents)

print("\nListing the file content in loop")
with open(filename) as file_objects:
    # contents = file_objects.read()

    for content in file_objects:
        print(content.rstrip())

print("\nStoring the file content in a list")
with open(filename) as file_objects:
    contents = file_objects.readlines()

for content in contents:
    line = content.strip().replace('Python', 'C')
    print(line)