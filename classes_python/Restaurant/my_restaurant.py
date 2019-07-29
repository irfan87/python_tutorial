from restaurant import Restaurant
from ice_cream_stand import IceCreamStand

my_restaurant = Restaurant('irfan restaurant', 'kelantan cuisine')

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