import json
import os

numbers = [1, 2, 3, 5]

filename = os.path.abspath('file_and_exceptions/json_practice/number.json')

# write the numbers variable as a json file
with open(filename, 'w') as file:
    json.dump(numbers, file)

# load numbers.json
with open(filename) as file:
    content = json.load(file)

print(content)