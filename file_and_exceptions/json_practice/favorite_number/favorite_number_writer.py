import os
import json

file_name = os.path.abspath('file_and_exceptions/json_practice/favorite_number/fav_number.json')

try:
    # load the json file
    with open(file_name) as json_file:
        json_content = json.load(json_file)
except FileNotFoundError:
    user_prompt = input("Please enter your favorite number: ")
    # write the file
    with open(file_name, 'w') as json_file:
        json.dump(user_prompt, json_file)

    print("To view the your favorite number, please run this app again.")
else:
    print("Your favorite number is:", json_content)