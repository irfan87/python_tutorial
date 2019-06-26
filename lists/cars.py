cars = ['honda', 'proton', 'kia', 'bmw']

for car in cars:
    if car == 'bmw' or car == 'kia':
        print(car.upper())
    else:
        print(car.title())

unwanted_cars = cars.pop(1)

message = f"{unwanted_cars.title()} was removed from your garage"

print(cars)
print(message)