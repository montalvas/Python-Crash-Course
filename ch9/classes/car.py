class Car():
    """Modelo de carro"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.gas_tank = 0
        
    def get_descriptive_name(self):
        """Retorna uma descrição do veículo"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """Imprime a quantidade de milhas no velocímetro"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
    def update_odometer(self, mileage):
        """Define a quantidade de milhas no velocímetro"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
            
    def increment_odometer(self, miles):
        """Incrementa a quantidade de milhas no velocímetro"""
        self.odometer_reading += miles
    
    def fill_gas_tank(self, liters):
        """Adiciona gasolina no tanque de combustível"""
        self.gas_tank += liters