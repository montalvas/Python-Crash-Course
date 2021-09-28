class Dog():
    """Modelando um cachorro"""
    def __init__(self, name, age):
        """Inicializa os atributos name e age.

        Args:
            name str: Nome do cachorro
            age int: Idade do cachorro
        """
        self.name = name
        self.age = age
    
    def sit(self):
        """Simula o comportamento de sentar de um cachorro"""
        print(self.name.title() + " is now sitting.")
    
    def roll_back(self):
        """Simula o comportamento de rolar com um comando"""
        print(self.name.title() + " rollend over!")