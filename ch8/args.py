# recebendo múltiplos argumentos (argumentos arbitrários)
# Os valores são armazenados em uma tupla

def make_pizza(*toppings):
    """[Cria uma pizza com os ingredientes solicitados]
    
    Args:
        *toppings (multiple): [ingredientes]
    """
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"\t- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# ordem dos parâmetros: posicionais, nomeados, arbitrários

def make_pizza(size, tomato_sauce=True, *toppings):
    """[Cria uma pizza com o tamanho e ingredientes solicitados]

    Args:
        size (str): [Tamanho da pizza]
        tomato_sauce (bool, optional): [Molho de tomate]. Defaults to True.
        *toppings (multiple): [ingredientes]
    """
    sauce = ""
    if tomato_sauce:
        sauce = "com molho de tomate"
    else:
        sauce = "sem molho de tomate"
    
    print(f"\nFazendo uma pizza {size} {sauce} e os seguintes ingredientes:")
    for topping in toppings:
        print(f"\t- {topping}")

make_pizza("Grande", "Atum", "Catupiry", "Milho", "Azeitona")
make_pizza("Media", False, "Palmito", "Mussarela", "Bacon")