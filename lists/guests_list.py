guests_list = ['ivy', 'abe e', 'emi', 'kak ju', 'abe di', 'danial', 'nina', 'amanda']

# insert the new guest that gonna attend the party!!!
guests_list.insert(0, 'abe mey')
guests_list.insert(1, 'abe ja')
guests_list.insert(2, 'papa')
guests_list.insert(3, 'mama')

# pop our the guest that cannot attend to the party
guests_absence_one = guests_list[1]
guests_absence_two = guests_list[0]

guests_list.remove(guests_absence_one)
guests_list.remove(guests_absence_two)

# replace the new guest to replace the absense guest
guests_list.append('abe sukimi')
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

remain_guest_message = f"{remain_guest_one.title()} and {remain_guest_two.title()} are still invited."
print(remain_guest_message)

del guests_absence_one
del guests_absence_two

print(guests_list)