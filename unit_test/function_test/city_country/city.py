from city_functions import get_city_country

print("Enter 'q', 'quit', 'Q', or 'Quit' to exit")

while True:
    user_prompt_city = input("Please enter your desired city: ")
    user_prompt_confirmation = ['q', 'quit', 'Quit', 'Q']

    if user_prompt_city in user_prompt_confirmation:
        print("Bye bye")

        break

    user_prompt_country = input("Please enter your desired country: ")

    if user_prompt_country in user_prompt_confirmation:
        print("Bye bye")

        break

    user_prompt_population = input("Please enter the population of your city (Optional): ")

    if user_prompt_population in user_prompt_confirmation:
        print("Bye bye")
        
        break

    city_country_name = get_city_country(user_prompt_city, user_prompt_country, user_prompt_population)

    print(city_country_name)
