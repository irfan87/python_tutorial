import os

filename = os.path.abspath("file_and_exceptions/pi_millions_digits.txt")

# filename = '/Users/nerve2009/Desktop/python_projects/python_crash_course/file_and_exceptions/pi_millions_digits.txt'

with open(filename) as pi_file:
    pi_lines = pi_file.readlines()

pi_string = ''

for pi_line in pi_lines:
    pi_string += pi_line.strip()

print(f"{pi_string[:52]}...")
print(len(pi_string))