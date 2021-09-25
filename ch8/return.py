# Valor de retorno

def get_formatted_name(first_name, last_name, middle_name=""):
    """[Devolve o nome completo formatado]

    Args:
        first_name ([str]): [Primeiro nome]
        last_name ([str]): [Sobrenome]
        middle_name (str, optional): [Nome do meio]. Defaults to "".

    Returns:
        [str]: [Nome completo formatado]
    """
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

myself = get_formatted_name("Lucas", "Albuquerque", "Montalvani")
my_son = get_formatted_name("Miguel", "Albuquerque")
print(myself)
print(my_son)

def build_person(first_name, last_name, age=''):
    """[Cria um dicionário contendo os dados de uma pessoa]

    Args:
        first_name ([str]): [Primeiro nome]
        last_name ([str]): [Segundo nome]
        age (str, optional): [idade]. Defaults to ''.

    Returns:
        [dict]: {'first': first_name, 'last': last_name}
    """
    
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
        
    return person

person1 = build_person("Adriana", "Lima")
print(person1)