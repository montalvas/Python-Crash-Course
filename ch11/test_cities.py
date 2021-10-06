import unittest
from unittest.case import TestCase
from city_functions import get_formatted_location


class CityTestCase(TestCase):
    """Testes para 'city_functions.py'"""
    
    def test_city_country_name(self):
        """Nomes como 'Santiago, Chile'"""
        location = get_formatted_location('Santiago', 'Chile')
        self.assertEqual(location, 'Santiago, Chile')
    
    def test_city_country_population_name(self):
        """Nomes como 'Santiago, Chile - população 500000."""
        location = get_formatted_location('Santiago', 'Chile', 500000)
        self.assertEqual(location, 'Santiago, Chile - População 500000.')


unittest.main()