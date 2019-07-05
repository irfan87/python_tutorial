number = input("Please enter your desire number: ")
number = int(number)

if number % 10 == 0:
    print(f"{number} is multiple by ten")
else:
    print(f"{number} is not multiple by ten")