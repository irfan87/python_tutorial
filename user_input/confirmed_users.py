# set unverified user as a list
unconfirmed_users = ['ivy', 'irfan', 'shukri', 'samad', 'ahmad']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed: ")

for confirmed_user in confirmed_users:
    print(f"{confirmed_user.title()}")

