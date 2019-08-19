import unittest
from city_functions import get_city_country

class NameTestCase(unittest.TestCase):
    """Test for 'city_functions.py'"""

    def test_city_country(self):
        city_country = get_city_country('johor baharu', 'johor')

        self.assertEqual(city_country, 'Johor Baharu, Johor')


    def test_city_country_population(self):
        city_country_population = get_city_country('johor bharu', 'johor', population=5000000)

        self.assertEqual(city_country_population, 'Johor Bharu, Johor - 5000000')

if __name__ == '__main__':
    unittest.main()