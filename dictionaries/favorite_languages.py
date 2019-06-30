favorite_languages = {
    'jen': 'python',
    'edward': 'ruby',
    'phil': 'python',
    'sarah': 'c',
    'jamal': 'java',
    'james': 'java',
    'hassan': 'php'
}

print("\nProgrammer with their favorite language polls")
for programmer_name, favorite_language in favorite_languages.items():
    if favorite_language == 'php':
        print(f"{programmer_name.title()} - {favorite_language.upper()}")
    else:
        print(f"{programmer_name.title()} - {favorite_language.title()}.")

print("\nProgrammer name list")
for programmer_name in favorite_languages:
    print(f"-> {programmer_name.title()}")

print("\nLanguages of choice")
for language in set(favorite_languages.values()):
    if language == 'php':
        print(language.upper())
    else:
        print(language.title())

print('\n')
programmers = ['jen', 'phil', 'josh', 'ali', 'abu', 'hassan']

for programmer_name in favorite_languages.keys():
    if programmer_name in programmers:
        fav_language = favorite_languages[programmer_name].title()
        
        print(f"{programmer_name.title()} love {fav_language.title()}")

print("\n")

# sorted programmers name who participate this polls
for programmer_name in sorted(favorite_languages.keys()):
    if programmer_name in favorite_languages.keys():
        print(f"Thanks for taking this poll, {programmer_name.title()}.")

print("\n")

for programmer in programmers:
    if programmer not in favorite_languages.keys():
        print(f"{programmer.title()}, mind to join this polls?")

if 'erin' not in favorite_languages.keys():
    print("\nHey, Erin! Please join with us in this poll")