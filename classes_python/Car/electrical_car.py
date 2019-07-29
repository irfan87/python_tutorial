from car import Car

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