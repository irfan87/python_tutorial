def build_person(first_name, last_name, age=None ,middle_name=''):
    if middle_name:
        person = {'first_name': first_name, 'middle_name': middle_name, 'last_name': last_name}
    else:
        person = {'first_name': first_name, 'last_name': last_name}

    if age:
        person['age'] = age

    return person

musician = build_person('jimi', 'hendrix', 27)
print(musician)

musician = build_person('john', 'hooker', 83, 'lee')
print(musician)

actor = build_person('will', 'smith', 50)
print(actor)