users_list = ['irfan', 'ikram', 'ivy', 'anuar', 'danial', 'nina', 'amanda', 'admin', 'john']
new_users = ['sarah', 'ikram', 'rizal', 'anuar', 'JOHN', 'Ivy']

current_users = [current_user.lower() for current_user in users_list]

for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"{new_user} is already taken\n")
    else:
        print(f"{new_user} is still available\n")

if users_list:
    for user in users_list:
        if user == 'admin':
            print("Hi, admin. would you like to see a status report?")
        else:
            print(f"Hello {user.title()}, thank you for logging in back")
else:
    print("We need to find more users")