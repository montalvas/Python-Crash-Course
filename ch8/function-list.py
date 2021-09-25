# Passando listas como parâmetro

def greet_users(names):
    for name in names:
        print(f"Hello, admiral {name.capitalize()}!")

admirals = ["Gohan", "Sengoku", "Aokiji", "Akainu", "Kyle", "Aioria"]
greet_users(admirals)
print()

# Modificando listas em uma função

def print_models(unprinted_designs, completed_models):
    """[Simula a criação de um modelo 3D]

    Args:
        unprinted_designs (list): [Lista com os designs]
        completed_models (list): [Lista com os modelos impressos]
    """
    while unprinted_designs:
        # simula a criação de uma impressão 3D a partir do design
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """[Mostra todos os modelos impressos]

    Args:
        completed_models (lista): [Lista com todos os modelos impressos]
    """
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print("\t" + completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)