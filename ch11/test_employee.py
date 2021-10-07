import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Teste para a classe Employee"""
    
    def setUp(self):
        """Cria um funcionário com nome, sobrenome e salário anual"""
        self.my_employee = Employee('Lucas', 'Montalvani', 36000)
        self.value = 12000    
    
    def test_default_give_raise(self):
        """Testa o aumento do salário anual com o valor default"""
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.annual_salary, 41000)
    
    def test_value_give_raise(self):
        """Testa o aumento do salário anual com um valor passado por parâmetro"""
        self.my_employee.give_raise(self.value)
        self.assertEqual(self.my_employee.annual_salary, 48000)


unittest.main()