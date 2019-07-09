def city_country(city_name, country_name):
    city = f"{city_name}, {country_name}"
    
    return city.title()

city_information = city_country('kota bharu', 'kelantan')
print(city_information)

city_information = city_country('kuala terengganu', 'terengganu')
print(city_information)

city_information = city_country('kuantan', 'pahang')
print(city_information)