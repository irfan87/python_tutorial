car = 'subaru'
item_to_buy = 'iphone'
house_needed_location = 'kuala lumpur'
users = ['kamal', 'james', 'samad']
other_user = 'samad'

print(car == 'subaru')
print(car == 'audi')
print(item_to_buy == 'iphone')
print(item_to_buy == 'watch')
print(house_needed_location == 'kuala lumpur'.title())
print(house_needed_location == 'kuala lumpur'.lower())
print(house_needed_location == 'kelantan')
print(users == 'hassan')
print(other_user == 'samad')

if users[-1] in users:
    print(f"{users[-1].title()}, you are on our list")