from datetime import date

class Users():
    """Modelo de dados de um usuário"""
    def __init__(self, first_name, last_name, nickname) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.nickname = nickname
        self.creation_date = date.today().strftime("%d/%m/%Y")
    
    def describe_user(self):
        """Inicializa os atributos que descrevem um perfil de usuário"""
        print(f"{self.nickname} profile:")
        print(f"\tFirst name: {self.first_name.capitalize()}")
        print(f"\tLast name: {self.last_name.capitalize()}")
        print(f"\tCreation date: {self.creation_date}")

    def greet_user(self):
        """Emite uma saudação personalizada ao usuário"""
        print(f"Welcome to our application, {self.nickname}.")