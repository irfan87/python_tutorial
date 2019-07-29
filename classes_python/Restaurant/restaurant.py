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