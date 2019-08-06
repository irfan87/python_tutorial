def cats_and_dogs(filename):
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"\nSorry, file {filename} is not found")
        # pass
    else:
        print(f"\nReading: {filename}")

        print(contents.title())

filenames = [
    '/Users/nerve2009/Desktop/python_projects/python_crash_course/file_and_exceptions/exceptions/cats.txt',
    '/Users/nerve2009/Desktop/python_projects/python_crash_course/file_and_exceptions/exceptions/dogs.txt',
    '/Users/nerve2009/Desktop/python_projects/python_crash_course/file_and_exceptions/exceptions/kitten.txt',  
]

for filename in filenames:
    cats_and_dogs(filename)