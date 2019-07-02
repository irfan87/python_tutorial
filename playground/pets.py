pets = []

pet = {
    'type': 'cat',
    'name': 'si tompok',
    'owner': 'samad',
    'age': 2,
    'food': 'meat'
}

pets.append(pet)

pet = {
    'type': 'fish',
    'name': 'shiny',
    'owner': 'ali',
    'age': 2,
    'food': 'fish food'
}

pets.append(pet)

pet = {
    'type': 'dog',
    'name': 'ember',
    'owner': 'ivy',
    'age': 3,
    'food': 'meat'
}

pets.append(pet)

# make a list of each pets
for pet in pets:
    animal_name = pet['name']

    print(f"\n{animal_name.title()}'s info:")

    for key, value in pet.items():
        print(f"{key} - {value}")