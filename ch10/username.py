import json


def get_stored_username():
    """Obtém nome do usuário já armazenado, caso disponível."""

    filename = 'name.json'
    try:
        with open(filename) as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return username


def set_username(name=''):
    """Cria e armazena o nome de usuário"""
    
    filename = 'name.json'
    
    if name:
        username = name
    else:
        username = input("What is your username? ")
    with open(filename, 'w') as file_object:
        json.dump(username, file_object)

    return username


def greet_user():
    """Sauda o usuário pelo nome"""

    username = get_stored_username()    
    if username == None:
        username = set_username()
        print(f"We'll remember you when you come back, {username}")
    else:
        current_user = input("Current user: ")
        if username == current_user:
            print(f"Wellcome back, {username}")
        else:
            username = set_username(current_user)
            print(f"Replaced user, {username}")
        

greet_user()
