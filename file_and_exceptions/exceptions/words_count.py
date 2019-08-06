def count_words(filename):
    try:
        # will open the file from the absolute path
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        # will raised an error if the file is not found or exist
        print(f"Sorry, {filename} is not exist")

        # will skip the errors if we use pass
        # pass
    else:
        # when the file found, the content of the file will split as an array and python will start counting the words per array
        words = contents.split()
        num_words = len(words)
        
        # python will message to us that the file will contained the words length
        print(f"The file {filename} has about {num_words} words.")

filenames = [
    '/Users/nerve2009/Desktop/python_projects/python_crash_course/file_and_exceptions/exceptions/alice.txt', 
    '/Users/nerve2009/Desktop/python_projects/python_crash_course/file_and_exceptions/exceptions/siddhartha.txt',
    '/Users/nerve2009/Desktop/python_projects/python_crash_course/file_and_exceptions/exceptions/moby_dick.txt',
    '/Users/nerve2009/Desktop/python_projects/python_crash_course/file_and_exceptions/exceptions/little_women.txt'
]

for filename in filenames:
    count_words(filename)