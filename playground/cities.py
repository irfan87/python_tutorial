cities = {
    'kuala lumpur': {
        'country': 'wilayah persekutuan kuala lumpur',
        'population': 3186000,
        'monument': 'klcc'
    },
    'kota bharu': {
        'country': 'kelantan',
        'population': 319600,
        'monument': 'stadium muhammad 4'
    }
}

for city_name, city_info in cities.items():
    print(f"\nAbout {city_name.title()}: ")

    city_country = city_info['country']
    city_population = str(city_info['population'])
    city_monument = city_info['monument']

    print(f" - Country: {city_country.title()}")
    print(f" - Population: {city_population}")
    print(f" - City Monument: {city_monument.title()}")