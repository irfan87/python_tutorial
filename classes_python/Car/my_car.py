from car import Car
from electrical_car import ElectricalCar

car = Car('audi', 'a4', '2019')
print(car.get_deceptive_name())

car.update_odometer(23_500)
car.read_odometer()

car.increment_odometer(100)
car.read_odometer()
car.fill_gas_tank()

print("\n")
tesla_car = ElectricalCar('tesla', 'model s', 2019)
print(tesla_car.get_deceptive_name())
tesla_car.battery.describe_battery()
tesla_car.fill_gas_tank()
tesla_car.battery.get_range()

print("\nMake an electric car and upgrade the battery if needed")
john_tesla = ElectricalCar('tesla', 'model 2', 2018)
john_tesla.battery.describe_battery()

print("\nUpgrade battery")
john_tesla.battery.battery_upgrade()
john_tesla.battery.describe_battery()

print("\nUpgrade battery status")
john_tesla.battery.battery_upgrade()
john_tesla.battery.describe_battery()