def get_city_country(city_name, country_name, population=0):
    city_country = f"{city_name}, {country_name}"

    if population:
        city_country = f"{city_name}, {country_name} - {population}"

    return city_country.title()