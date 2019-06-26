# eligible_age = 18
eligible_age = input("please enter your age:")

age = int(eligible_age)

if age < 21:
    print("You may not be able to enter to this club")
elif age >= 21:
    print("You may enter to this club")