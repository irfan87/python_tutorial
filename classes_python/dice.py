from random import randint

class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_dice(self):
        return randint(1, self.sides)

dice_six = Dice(6)

results = []

for roll_num in range(10):
    result = dice_six.roll_dice()
    results.append(result)

print("10 rolls of a 6-sided dice")
print(results)

dice_ten = Dice(10)

results = []

for roll_num in range(10):
    result = dice_ten.roll_dice()
    results.append(result)

print("\n10 rolls of a 10-sided dice")
print(results)

dice_twenty = Dice(20)

results = []

for roll_num in range(10):
    result = dice_twenty.roll_dice()
    results.append(result)

print("\n10 rolls of a 20-sided dice")
print(results)