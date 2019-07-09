# function of describe_city() with the name of the city and the state of the city as the default paramaeter
def describe_city(city_name, country_name='kelantan'):
    if 'us' in country_name:
        print(f"\n{city_name.title()} is in {country_name.upper()}")
    else:
        print(f"\n{city_name.title()} is in {country_name.title()}")

# called out the describe_city function with the default parameter
describe_city('kota bharu')
describe_city("kubang kerian")

# called out the describe_city function without the default parameter
describe_city('kuala terengganu', 'terengganu')