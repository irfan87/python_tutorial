filename = '/Users/nerve2009/Desktop/python_projects/python_crash_course/file_and_exceptions/programming.txt'

with open(filename, 'w') as f:
    f.write("I love Programming so damn much!!\n")
    f.write("I really want to make an awesome application with Python\n")

with open(filename, 'a') as f:
    f.write("I also love finding meaning in large datasets.\n")
    f.write("I am looking forward to do like a data-scientist do.\n")

# open file
with open(filename, 'r') as f:
    contents = f.read()

print(contents)
