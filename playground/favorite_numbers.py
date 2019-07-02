favorite_numbers = {
    'irfan': [15, 5, 20],
    'james': [20, 10, 1],
    'ivy': [10, 3, 4],
    'amanda': [5, 50, 100],
    'danial': [35, 60, 100]
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite number is: ")

    for number in numbers:
        print(f"- {str(number)}")