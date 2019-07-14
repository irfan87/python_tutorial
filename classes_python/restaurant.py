class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"\n{self.restaurant_name.title()} is serving {self.cuisine_type.title()}")

    def open_restaurant(self):
        print(f"\n{self.restaurant_name.title()} is opening now!\n")

my_restaurant = Restaurant('irfan restaurant', 'kelantan cuisine')
ivy_restaurant = Restaurant('ivy restaurant', 'chinese cuisine')

print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

print(ivy_restaurant.restaurant_name)
ivy_restaurant.describe_restaurant()