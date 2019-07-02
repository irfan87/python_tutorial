favorite_places = {
    'john': ['paris', 'singapore', 'japan'],
    'jane': ['seoul', 'kuala lumpur', 'thailand'],
    'doe': ['paris', 'india', 'china']
}

for name, places in favorite_places.items():
    print(f"{name.title()} favorite places: ")

    for fav_place in places:
        print(f"\t{fav_place.title()}")