class Employee():
    """Classe que representa um funcionário
    
    Methods:
        __init__ : inicia os métodos da classe
        give_raise : soma um valor ao salário anual
            
    """
    
    def __init__(self, name, lastname, annual_salary) -> None:
        """Inicia os atributos da classe

        Args:
            name (str): Nome do funcionário
            lastname (str): Sobrenome do funcionário
            annual_salary (str): Salário anual
        """
        self.name = name
        self.lastname = lastname
        self.annual_salary = annual_salary
        
    def give_raise(self, value = 5000):
        """Soma um valor ao salário anual"""
        self.annual_salary += value
    
    
    