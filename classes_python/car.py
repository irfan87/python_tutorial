class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_deceptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"

        return long_name.title()

    def read_odometer(self):
        print(f"this car has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print(f"This car can fill the gas")

class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has {self.battery_size}-kWh battery")

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on full charge")

    def battery_upgrade(self):
        if self.battery_size == 75:
            self.battery_size = 90
            print("The battery is using 90 kWh.")
        else:
            print("The battery is already upgraded")

class ElectricalCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        print(f"This car can not fill the gas")

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