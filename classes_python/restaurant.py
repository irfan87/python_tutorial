# parent class
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"\n{self.restaurant_name.title()} is serving {self.cuisine_type.title()}")

    def open_restaurant(self):
        print(f"\n{self.restaurant_name.title()} is opening now!\n")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        self.number_served += additional_served

# child class (IceCreamStand) inherit from the parent class (Restaurant)
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type='ice_cream'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def show_ice_cream_flavor(self):
        for flavor in self.flavors:
            print(f"{flavor.title()}")

my_restaurant = Restaurant('irfan restaurant', 'kelantan cuisine')
ivy_restaurant = Restaurant('ivy restaurant', 'chinese cuisine')

print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

print(f"\nNumber served: {str(my_restaurant.number_served)}")
my_restaurant.number_served = 123
print(f"\nNumber served: {str(my_restaurant.number_served)}\n")

my_restaurant.set_number_served(1506)
print(f"\nNumber served: {str(my_restaurant.number_served)}\n")

my_restaurant.increment_number_served(20)
print(f"\nNumber served: {str(my_restaurant.number_served)}\n")

magnum_stand = IceCreamStand('magnum ice cream stand')
magnum_stand.flavors = ['chocolate', 'vanilla', 'black chocolate']

magnum_stand.describe_restaurant()
magnum_stand.show_ice_cream_flavor()
print("\n")

print(ivy_restaurant.restaurant_name)
ivy_restaurant.describe_restaurant()