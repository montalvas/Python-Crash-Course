class Restaurant():
    """Modelo de um restaurante
    
    Methods:
        __init__ -> Inicializa os atributos
                
        describe_restaurant -> Imprime descrição do restaurante
        
        open_restaurant -> Imprime que o restaurante está aberto
        
        get_number_served -> Imprime a quantidade de clientes servidos
        
        set_number_served -> Define a quantidade de clientes servidos
        
        increment_number_served -> Incrementa a quantidade de clientes servidos
    """ 
    
    def __init__(self, restaurant_name, cuisine_type) -> None:
        """Inicializa os atributos

        Args:
            restaurant_name (str): Nome do restaurante
            cuisine_type (str): Tipo de cozinha
        Self:
            number_served (int): Número de clientes servidos
        """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        """Imprime o nome e a especialidade do restaurante"""
        print(f"\nRestaurant name: {self.restaurant_name}.")
        print(f"Cuisine type: {self.cuisine_type}")
    
    def open_restaurant(self):
        """Imprime que o restaurante está aberto"""
        print(f"\nThe {self.restaurant_name} is open.")
    
    def get_number_served(self):
        """Imprime o número de clientes servidos"""
        print(f"\nThe restaurant served {self.number_served} clients.")
    
    def set_number_served(self, number):
        """Define o número de clientes servidos

        Args:
            number (int): Número de clientes servidos
        """
        if number >= 0:
            self.number_served = number
        else:
            print("You can't serve a negative number.")
    
    def increment_number_served(self, increment):
        """Incrementa a quantidade de clientes servidos

        Args:
            increment (int): [Valor de incremento]
        """
        if increment >= 0:
            self.number_served += increment
        else:
            print("You can't increment a negative number.")