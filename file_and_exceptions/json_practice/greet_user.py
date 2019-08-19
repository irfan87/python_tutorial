'''
we will load the same json file from username.json as we greet to the user.
'''

import os
import json

filename = os.path.abspath('file_and_exceptions/json_practice/username.json')

with open(filename, 'r') as file:
    user = json.load(file)

print(f"We meet again, {user.title()}!")