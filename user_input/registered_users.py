# create a registered users list
registered_users = ['james', 'jane', 'doe']

#  create an empty confirm registered user list
confirmed_registered_users = []

while registered_users:
    current_user = registered_users.pop()
    print(f"Below is registered users but not confirmed yet: {current_user.title()}")

    confirmed_registered_users.append(current_user)

print("\nBelow is the confirmed registered users: ")

for index, confirmed_registered_user in enumerate(confirmed_registered_users, start=1):
    print(index, confirmed_registered_user.title())