def montar_sanduiche(*ingredientes):
    """[Monta um sanduíche com os ingredientes passados]
    
    *Args:
        ingredientes (str): Ingrediente para o sanduiche
    """
    if ingredientes:
        print("\nMontando o sanduiche com:")
        for ingrediente in ingredientes:
            print(f"\t- {ingrediente}")
    else:
        print("\nSem ingredientes para montar o sanduiche.")

montar_sanduiche("Rosbife", "Molho Teryiaki", "Queijo Parmesao", "Rucula", "Picles")
montar_sanduiche("Frango com cream cheese", "Batata palha", "Molho de mostarda e mel")
montar_sanduiche()

def make_car(car_brand, car_model, **optionals):
    """[Make a car with a bunch of specifications]

    Args:
        manufacturer (str): Car brand
        model (str): Car model
    *Kwargs:
        optionals (key, value): field => value
    Returns:
        dict: {brand: car_brand, model: car_model, key: value}
    """
    produced_car = {'brand': car_brand, 'model': car_model}
    for key, value in optionals.items():
        produced_car[key] = value
    
    return produced_car

print()
print(make_car("Mitsubishi", "Eclipse", color="Black", year="2021"))
print(make_car("BMW", "IX", color="Red", year="2022"))
