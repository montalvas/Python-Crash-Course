import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Testes para 'name_function.py'."""

    def test_first_last_name(self):
        """Nomes como 'Ada Lovelace'"""
        formatted_name = get_formatted_name('Ada', 'Lovelace')
        self.assertEqual(formatted_name, 'Ada Lovelace')
    
    def test_first_middle_last_name(self):
        """Nomes como 'Ada Byron King'"""
        formatted_name = get_formatted_name('ada', 'king', 'byron')
        self.assertEqual(formatted_name, 'Ada Byron King')


unittest.main()
