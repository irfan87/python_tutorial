number = input("Please enter a number, and I will tell you if it is odd or even: ")
number = int(number)

if number % 2:
    print(f"The {number} is odd")
else:
    print(f"The {number} is even")