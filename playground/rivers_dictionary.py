famous_rivers = {
    'kelantan river': 'kelantan',
    'sarawak river': 'sarawak',
    'selangor river': 'selangor'
}

message_title = '\nfamous rivers in malaysia'

print(message_title.title())

# loop all Malaysian famous rivers here
print("\nEach rivers in each state")
for river, state in famous_rivers.items():
    river_in_country = f"{river.title()} - {state.title()}"
    print(river_in_country)

# loop all states 
print("\nStates name")
for state in famous_rivers.values():
    state_name = f"{state.title()}"
    print(state_name)

# loop all rivers
print("\nRivers name")
for river in famous_rivers.keys():
    river_name = f"{river.title()}"
    print(river_name)