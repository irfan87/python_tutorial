numbers = range(1, 21)

print("even number:".title())
for number in list(numbers):
    if(number % 2) == 0:
        print(number)

print("\nodd numbers:".title())
for number in list(numbers):
    if (number % 2) == 1:
        print(number)