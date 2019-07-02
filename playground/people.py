# make a list of people dictionary
people = []

person = {
    'first_name': 'ahmad irfan',
    'last_name': 'mohammad shukri',
    'age': 32,
    'job': 'web developer'
}

people.append(person)

person = {
    'first_name': 'ivy',
    'last_name': 'ying',
    'age': 21,
    'job': 'hair dresser'
}

people.append(person)

person = {
    'first_name': 'james',
    'last_name': 'edward',
    'age': 32,
    'job': 'youtube vlogger'
}

people.append(person)

for person in people:
    full_name = f"{person['first_name'].title()} {person['last_name'].title()}"
    age = f"{person['age']}"
    job = f"{person['job'].title()}"

    print(f"\nFullname: {full_name}\nAge: {age}\nJob: {job}")