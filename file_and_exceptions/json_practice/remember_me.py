'''
This will store the user's name as the json file.
Also will generate the json file - username.json and reused it as a greeter.
'''

import json
import os

filename = os.path.abspath('file_and_exceptions/json_practice/username.json')

def get_stored_username():
    try:
        with open(filename) as file:
            username = json.load(file)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input("Please type your name: ")
    
    with open(filename, 'w') as file:
        json.dump(username, file)

    return username

def greet_user():
    username = get_stored_username()

    if username:
        correct_username = input(f"Are you sure your username is {username}? (y/n) ")
        user_prompt_answer = ['y', 'yes', 'Y', 'Yes']

        if correct_username in user_prompt_answer:
            print(f"Welcome back, {username.title()}!")
        else:
            # print("Invalid username")
            username = get_new_username()
            print(f"Goodbye, {username.title()}. See you later, again!")
    else:
        username = get_new_username()
        print(f"Goodbye, {username.title()}. See you later!")

greet_user()