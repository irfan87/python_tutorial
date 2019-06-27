# make a users list
users = ['ivy', 'amanda', 'nina', 'brock', 'jimmy', 'carragher']

# insert new user in the list
users.append('james')
users.append('colby')
users.append('sam')

# sorted users as alphabetical
users.sort()

# get the last four users
for user in list(users[4:]):
    print(user)

# checked if certain user is in the list
if 'johnny' not in users:
    print("johnny is not in your list")
else:
    print("johnny is in your list")
