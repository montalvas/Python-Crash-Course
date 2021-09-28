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
    
    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}.")
        print(f"Cuisine type: {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"The {self.restaurant_name} is open.")