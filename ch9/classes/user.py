from datetime import date

class User():
    """Modelo de perfil de usuário
    
    Methods:
        __init__ -> Inicializa os atributos
                
        describe_user -> Imprime as informações do perfil
        
        greet_user -> Imprime uma saudação ao usuário
        
        increment_login_attempts -> Incrementa o número de logins do usuário
        
        reset_login_attempts -> Reseta o número de logins do usuário
        """
    
    def __init__(self, first_name, last_name, nickname) -> None:
        """Inicia os atributos

        Args:
            first_name (str): Primeiro nome
            last_name (str): Último nome
            nickname (str): Nome de usuário
        Self:
            creation_date (str, default=Today): Data de criação
            login_attempts (int, default=0): Número de login feito pelo usuário
        """
        self.first_name = first_name
        self.last_name = last_name
        self.nickname = nickname
        self.creation_date = date.today().strftime("%d/%m/%Y")
        self.login_attempts = 0
    
    def describe_user(self):
        """Imprime as informações do perfil do usuário"""
        print(f"\n{self.nickname} profile:")
        print(f"\tFirst name: {self.first_name.capitalize()}")
        print(f"\tLast name: {self.last_name.capitalize()}")
        print(f"\tCreation date: {self.creation_date}")
        print(f"\tLogin attempts: {self.login_attempts}")

    def greet_user(self):
        """Emite uma saudação personalizada ao usuário"""
        print(f"Welcome to our application, {self.nickname}.")
    
    def increment_login_attempts(self):
        """Incrementa a quantidade de logins"""
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """Reseta a quantidade de logins"""
        self.login_attempts = 0