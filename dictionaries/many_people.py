# dictionaries in dictionaries implementations
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
    }
}

for username, user_info in users.items():
    print(f"Username: {username}")
    fullname = f"{user_info['first']} {user_info['last']}"
    location = f"{user_info['location']}"

    print(f"\tUser's fullname: {fullname.title()}")
    print(f"\tUser's location: {location.title()}")