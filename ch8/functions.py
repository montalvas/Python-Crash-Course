# Funções são blocos de código nomeados que realizam uma tarefa específica.

def greet_user():
    """[Exibe uma saudação simples]"""
    print("Hello!")

greet_user()

def greet_user(username):
    """[Exibe uma saudaçaõ simples]

    Args:
        username ([string]): [Pessoa a cumprimentar]
    """
    print(f"Hello, {username.capitalize()}!")

greet_user('miguel')
greet_user('adriana')

def favorite_book(title):
    """[Exibe meu livro favorito]

    Args:
        title ([string]): [livro]
    """
    print(f"My favorite book is {title.capitalize()}.")

favorite_book("Tons de magia")