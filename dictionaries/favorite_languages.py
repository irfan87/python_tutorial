favorite_languages = {
    'jen': 'python',
    'edward': 'ruby',
    'phil': 'python',
    'sarah': 'c',
    'jamal': 'java',
    'james': 'java'
}

print("\nProgrammer with their favorite language polls")
for programmer_name, favorite_language in favorite_languages.items():
    print(f"{programmer_name.title()} - {favorite_language.title()}.")

print("\nProgrammer name list")
for programmer_name in favorite_languages:
    print(f"-> {programmer_name.title()}")

print("\nLanguages of choice")
for language in set(favorite_languages.values()):
    print(language.title())

programmers = ['jen', 'phil']

for programmer_name in favorite_languages.keys():
    if programmer_name in programmers:
        fav_language = favorite_languages[programmer_name].title()

        print(f"\n{programmer_name.title()} love {fav_language.title()}")

# sorted programmers name who participate this polls
for programmer_name in sorted(favorite_languages.keys()):
    print(f"\n{programmer_name.title()}, thanks for taking this poll.")

if 'erin' not in favorite_languages.keys():
    print("\nHey, Erin! Please join with us in this poll")