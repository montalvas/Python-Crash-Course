from classes.user import User
from classes.privileges import Privileges


class Admin(User):
    """Modelo de perfil de administrador

    Methods:
        __init__ -> Inicializa os atributos da classe pai e da própria classe

        describe_user -> Imprime as informações do perfil

        greet_user -> Imprime uma saudação ao usuário

        increment_login_attempts -> Incrementa o número de logins do usuário

        reset_login_attempts -> Reseta o número de logins do usuário

        show_privileges -> Mostra os privilégios do administrador
        """

    def __init__(self, first_name, last_name, nickname) -> None:
        super().__init__(first_name, last_name, nickname)
        self.privileges = Privileges()
