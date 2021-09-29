class Battery():
    """Modelo de bateria de carro elétrico"""
    
    def __init__(self, battery_size=70):
        """Inicializa os atributos da bateria"""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Descreve a capacidade da bateria"""
        print(f"This car has a {self.battery_size}-KWh battery.")
    
    def get_range(self):
        """Imprime a distância que o carro é capaz de percorrer com
        essa bateria"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        
        message = f"This car can go approximately {range} miles on a full charge."
        print(message)