aliens = []

for aliens_number in range(30):
    new_alien = {
        'color': 'green',
        'points': 5,
        'speed': 'slow'
    }

    aliens.append(new_alien)

for alien in aliens[:4]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'

for alien in aliens[:10]:
    print(alien)

print("...")

print(f"Total number of aliens: {len(aliens)}")