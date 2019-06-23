players = ['charles', 'martina', 'michael', 'michelle', 'florence', 'eli']

print(players[0:2]) # charles and martina will showed up
print(players[1:4]) # martina micheal and michelle will showed up
print(players[:4]) # start from the beginning - 0 to 4
print(players[2:]) # start from id 2 to the end of the list
print(players[-3:]) # michelle, florence and eli will showed up
print(players[-2:]) # florence and eli will showed up

print("Here are the first three players on my team:")
for player in players[0:3]:
    print(player.title())