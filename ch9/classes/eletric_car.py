from classes.car import Car

class EletricCar(Car):
    """Modelo de veículo elétrico"""
    
    def __init__(self, make, model, year):
        """Inicializa os atributos da classe pai
        Em seguida, inicializa os atributos específicos de um carro elétrico
        """
        super().__init__(make, model, year)
        self.battery_size = 70
        
    def describe_battery(self):
        """Exibe a capacidade da bateria"""
        print(f"\nThis car has a {self.battery_size}-KWh battery.")