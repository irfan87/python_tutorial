name = input("Please enter your name: ")

filename = '/Users/nerve2009/Desktop/python_projects/python_crash_course/file_and_exceptions/guests.txt'

with open(filename, 'w') as f:
    f.write(name.title())