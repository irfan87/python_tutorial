filename = '/Users/nerve2009/Desktop/python_projects/python_crash_course/file_and_exceptions/pi_millions_digits.txt'

with open(filename) as pi_file:
    pi_lines = pi_file.readlines()

    pi_string = ''

    for pi_line in pi_lines:
        pi_string += pi_line.strip()

    birthday = input("Enter your birthday, in the form mmddyy: ")

    if birthday in pi_string:
        print("Your birthday is in the million's pi")
    else:
        print("Your birthday is not in in the million's pi")