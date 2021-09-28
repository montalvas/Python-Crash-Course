class Restaurant():
    """Modelando um restaurante"""
    def __init__(self, restaurant_name, cuisine_type) -> None:
        """Inicializa os atributos restaurant_name e cuisine_type

        Args:
            restaurant_name (str): Nome do restaurante
            cuisine_type (str): Tipo de cozinha
        """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"\nRestaurant name: {self.restaurant_name}.")
        print(f"Cuisine type: {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"\nThe {self.restaurant_name} is open.")
    
    def get_number_served(self):
        print(f"\nThe restaurant served {self.number_served} clients.")
    
    def set_number_served(self, number):
        if number >= 0:
            self.number_served = number
        else:
            print("You can't serve a negative number.")
    
    def increment_number_served(self, increment):
        if increment >= 0:
            self.number_served += increment
        else:
            print("You can't increment a negative number.")