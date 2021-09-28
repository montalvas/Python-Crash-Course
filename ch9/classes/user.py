from datetime import date

class Users():
    """Modelo de dados de um usuário"""
    def __init__(self, first_name, last_name, nickname) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.nickname = nickname
        self.creation_date = date.today().strftime("%d/%m/%Y")
        self.login_attempts = 0
    
    def describe_user(self):
        """Inicializa os atributos que descrevem um perfil de usuário"""
        print(f"\n{self.nickname} profile:")
        print(f"\tFirst name: {self.first_name.capitalize()}")
        print(f"\tLast name: {self.last_name.capitalize()}")
        print(f"\tCreation date: {self.creation_date}")
        print(f"\tLogin attempts: {self.login_attempts}")

    def greet_user(self):
        """Emite uma saudação personalizada ao usuário"""
        print(f"Welcome to our application, {self.nickname}.")
    
    def increment_login_attempts(self):
        """Incrementa o login attempts em 1"""
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """Reseta o valor de login attempts"""
        self.login_attempts = 0