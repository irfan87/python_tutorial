from restaurant import Restaurant

# child class (IceCreamStand) inherit from the parent class (Restaurant)
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type='ice_cream'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def show_ice_cream_flavor(self):
        for flavor in self.flavors:
            print(f"{flavor.title()}")