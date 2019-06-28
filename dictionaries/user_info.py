user_info = {
    'username': 'irfan87',
    'first_name': 'ahmad irfan',
    'last_name': 'mohammad shukri'
}

for key, value in user_info.items():
    if value == 'irfan87':
        print(f"\n{key}: {value.lower()}")
    else:
        print(f"\n{key}: {value.title()}")