filename = '/Users/nerve2009/Desktop/python_projects/python_crash_course/file_and_exceptions/pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''

for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))