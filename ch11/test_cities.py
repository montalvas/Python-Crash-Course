import unittest
from unittest.case import TestCase
from city_functions import get_formatted_location


class CityTestCase(unittest.TestCase):
    """Testes para 'city_functions.py'"""
    
    def test_city_country_name(self):
        """Nomes como 'Santiago, Chile'"""
        location = get_formatted_location('Santiago', 'Chile')
        self.assertEqual(location, 'Santiago, Chile')


unittest.main()