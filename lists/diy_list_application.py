# a simple application that show the list of my friends
# it will have the existing friends and new friends

# TODO: list of my existing friends
my_existing_friends = ['ivy', 'nick', 'sol', 'amin', 'sham', 'wan', 'aiman']

print(my_existing_friends)

# TODO: send greetings to each friend
my_friend = my_existing_friends[0]
greeting_msg = f"Hi, {my_friend.title()}"
print(greeting_msg)

my_friend = my_existing_friends[1]
greeting_msg = f"Hi, {my_friend.title()}"
print(greeting_msg)

my_friend = my_existing_friends[2]
greeting_msg = f"Hi, {my_friend.title()}"
print(greeting_msg)

my_friend = my_existing_friends[3]
greeting_msg = f"Hi, {my_friend.title()}"
print(greeting_msg)

my_friend = my_existing_friends[4]
greeting_msg = f"Hi, {my_friend.title()}"
print(greeting_msg)

my_friend = my_existing_friends[5]
greeting_msg = f"Hi, {my_friend.title()}"
print(greeting_msg)

my_friend = my_existing_friends[6]
greeting_msg = f"Hi, {my_friend.title()}"
print(greeting_msg)

# TODO: remove any friend that not contact anymore
my_friend = my_existing_friends[6]
print(f"\nSo sad because {my_friend.title()} and I not friend anymore")
del my_existing_friends[6]

# TODO: replace new friend
my_existing_friends.insert(6, 'malik')
my_friend = my_existing_friends[6]
greeting_msg = f"\n{my_friend.title()} is my new friend"
print(greeting_msg)

# add some more new friends
print("\nWe are homies!!")

# TODO: insert new friends from the beginning, in the middle and the last position
my_existing_friends.insert(0, 'amelin')
my_existing_friends.insert(2, 'khairul')
my_existing_friends.insert(-1, 'mamat')

my_new_friend = my_existing_friends[0]
greeting_msg = f"Hi, {my_new_friend.title()}, my new friend!"
print(greeting_msg)

my_new_friend = my_existing_friends[2]
greeting_msg = f"Hi, {my_new_friend.title()}, my new friend!"
print(greeting_msg)

my_new_friend = my_existing_friends[8]
greeting_msg = f"Hi, {my_new_friend.title()}, my new friend!"
print(greeting_msg)

# TODO: make your list a lil bit smaller
lost_contact_friend = my_existing_friends.pop(3)
message = f"\nMe and {lost_contact_friend.title()} are still friend but not frequent contact\n"
print(message)

print(my_existing_friends)

# TODO: sort your friends with sorted as alphabetical
sorted_my_friends = sorted(my_existing_friends)
print(f"\nSorted list: {sorted_my_friends}")

# TODO: reverse your sorted friends as a original list
sorted_my_friends = sorted(my_existing_friends, reverse=True)
print(f"Reverse to original list: {sorted_my_friends}")

# TODO: show the world the size of your friends
my_friends_size = len(my_existing_friends)
message = f"\nI have {my_friends_size} friends in my contact\n"
print(message)