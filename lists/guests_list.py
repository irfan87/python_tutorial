guests_list = []

# insert the new guest that gonna attend the party!!!
guests_list.insert(0, 'anuar')
guests_list.insert(1, 'rizal')
guests_list.insert(2, 'shukri')
guests_list.insert(3, 'zaleha')
guests_list.insert(4, 'ivy')
guests_list.insert(5, 'amelin')

# pop our the guest that cannot attend to the party
guests_absence_one = guests_list[1]
guests_absence_two = guests_list[0]

guests_list.remove(guests_absence_one)
guests_list.remove(guests_absence_two)

# replace the new guest to replace the absense guest
guests_list.append('sukimi')
guests_list.append('john')

# send another three guests an invitation
guests_list.insert(0, 'sam')
guests_list.insert(1, 'colby')
guests_list.append('Jake')
    
absence_message = f"{guests_absence_one.title()} and {guests_absence_two.title()} are unable to attend to your dinner party.\n"

print(absence_message)

# send invitation message to the invited guests
for guest in guests_list:
    invitation_message = f"Hi, {guest.title()}! You are invited to join the dinner party.\n"
    
    print(invitation_message)

rejection_guest = guests_list.pop(-1)
rejection_message = f"Sorry, {rejection_guest}. You are not invited to the dinner party because of you are late.\n"

if rejection_guest :
    print(rejection_message)

# make sure colby and sam are still invited
remain_guest_one = guests_list[0]
remain_guest_two = guests_list[1]

remain_guest_message = f"{remain_guest_one.title()} and {remain_guest_two.title()} are still invited.\n"

print(remain_guest_message)

remove_guest_one = guests_list[0]
remove_guest_two = guests_list[1]

del remove_guest_one
del remove_guest_two

# sort guests as alphabet
guests_list.sort()

# show the invited guests
invited_guests_length = len(guests_list)
admin_message = f"Invited guests: {invited_guests_length}"

print(admin_message)