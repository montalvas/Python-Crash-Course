# Argumentos posicionais

def describle_pet(animal_type, pet_name):
    """[Exibe informações sobre o animal de estimação]

    Args:
        animal_type ([string]): [Qual o tipo do animal]
        pet_name ([string]): [Nome do animal]
    """
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.capitalize()}.")

describle_pet('cat', 'barney')
describle_pet('turtle', 'margarida')

# Argumentos nomeados (Ao nomear o argumento, não importa a ordem)

describle_pet(pet_name='kit kat', animal_type='cat')

# Valor Default (deve sempre ser alocado após os argumentos posicionados)

def describle_pet(pet_name ,animal_type='cat'):
    """[Descreve o animal de estimação]

    Args:
        pet_name ([string]): [Nome do animal]
        animal_type (str, optional): [Tipo do animal]. Defaults to 'cat'.
    """
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.capitalize()}.")

describle_pet("Luke")