# create a person's dictionary list
person = {
    'first_name': 'ahmad irfan',
    'last_name': 'mohammad shukri',
    'age': 32,
    'city': 'kota bharu'
}

person_first_name = person['first_name']
person_last_name = person['last_name']
person_age = person['age']
person_city_live = person['city']

# print out person's information
print("Personal Information")
print(f"First Name: {person_first_name.title()}")
print(f"Last Name: {person_last_name.title()}")
print(f"Age: {person_age}")
print(f"City Live: {person_city_live.title()}")