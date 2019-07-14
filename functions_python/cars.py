def make_car(car_manufacturer, car_model, **car_options):
    car_dictionary = {
        'car_manufacturer': car_manufacturer.title(),
        'car_model': car_model.title()
    }

    for option, value in car_options.items():
        car_dictionary[option] = value

    return car_dictionary

car = make_car('subaru', 'outback', color='blue', tow_package=True)

print(car)

car = make_car('honda', 'accord', year=1991, color='white', headlights='popup')
print(car)