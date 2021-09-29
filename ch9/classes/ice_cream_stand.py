from classes.restaurant import Restaurant

class IceCreamStand(Restaurant):
    """Modelo de uma sorveteria
    
    __Methods:
        __init__ -> Inicializa os atributos
                
        describe_restaurant -> Imprime descrição do restaurante
        
        open_restaurant -> Imprime que o restaurante está aberto
        
        get_number_served -> Imprime a quantidade de clientes servidos
        
        set_number_served -> Define a quantidade de clientes servidos
        
        increment_number_served -> Incrementa a quantidade de clientes servidos
        
        show_flavors -> Imprime os sabores de sorvete
    """    
    
    def __init__(self, restaurant_name, cuisine_type) -> None:
        """Inicializa os atributos da classe pai e da própria classe.

        Args:
            restaurant_name (str): Nome do restaurante
            cuisine_type (str): Especialidade do restaurante
        Self:
            flavors (list of str): Lista de sabores
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['morango', 'chocolate', 'baunilha', 'castanha', 'coco']
        """lista de str: Contém os sabores dos sorvetes"""
    
    def show_flavors(self):
        """Imprime os sabores de sorvete"""
        print("\nThe ice cream flavors are:")
        for flavor in self.flavors:
            print(f"\t{flavor}")