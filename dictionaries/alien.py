# define the low level alien as the dictionary
alien = {}

alien['colors'] = 'green'
alien['x_position'] = 0
alien['y_position'] = 25
alien['speed'] = 'medium'

print(f"Alien original position: {alien['x_position']}")
# determine the alien's speed
if alien['speed'] == 'slow':
    x_increment = 1
elif alien['speed'] == 'medium':
    x_increment = 2
elif alien['speed'] == 'fast':
    x_increment = 3

alien['x_position'] += x_increment

print(f"Alien new position: {alien['x_position']}")

point_values = alien.get('scores', 'No point value assigned')
print(point_values)