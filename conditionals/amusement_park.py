print("Welcome to my amusement park!\n")
age = input("Before that, please tell us your age: ")

if int(age) < 4:
    price = 0
elif int(age) < 18:
    price = 25
elif int(age) < 65:
    price = 40
elif int(age) >= 65:
    price = 20

if price == 0:
    print("Admission cost: Free")
else:
    print(f"Admission cost: ${price}")

print("Have fun!!!")