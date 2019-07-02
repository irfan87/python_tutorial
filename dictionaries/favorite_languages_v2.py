favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    'hassan': ['java', 'php']
}

# loop all the favorite languages per programmers 
for name, language in favorite_languages.items():
    print(f"\n{name} favorite languages are: ")

    for fav_language in language:
        if fav_language == 'php':
            print(f"-> {fav_language.upper()}")
        else:
            print(f"-> {fav_language.title()}")