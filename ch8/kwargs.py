# multiplos argumentos nomeados
# Os valores são armazenados em um dicionário

def cidadeEstado(**kwargs):
    print(kwargs)

cidadeEstado(SE="Itabaiana", SP="Sao Paulo")

def build_profile(first, last, **user_info):
    """Cria um perfil de usuário

    Args:
        first (str): Primeiro nome
        last (str): Sobrenome
    **Kwargs:
        user_info (key, value), optional: Campo => Valor  
    Returns:
        dict: {first_name: first, last_name: last, key: value...}
    """
    profile = {}
    profile['first_name'] = first.capitalize()
    profile['last_name'] = last.capitalize()
    for key, value in user_info.items():
        profile[key] = value.capitalize()
    return profile

user_profile = build_profile('lucas', 'albuquerque', age='27', gender='male')
print(user_profile)