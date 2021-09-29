class Privileges():
    """Modelo de privilégios do usuário"""
    
    def __init__(self) -> None:
        """Inicia os atributos
        
        Self:
            privileges (list of str): Lista de privilégios do usuário
        """
        
        self.privileges = ["can add post", "can delete post", "can ban user"]
    
    def show_privileges(self):
        """Imprime os privilégios do usuário"""
        
        print(f"\nList of privileges of a admin user:")
        for privilege in self.privileges:
            print(f"\t{privilege}")