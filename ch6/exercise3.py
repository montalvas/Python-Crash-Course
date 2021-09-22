pets = []

simba = {
    'tipo': 'leão',
    'dono': 'lucas',
}

barney = {
    'tipo': 'gato',
    'dono': 'miguel',
}

margarida = {
    'tipo': 'tartaruga',
    'dono': 'adriana',
}

pets.append(simba)
pets.append(barney)
pets.append(margarida)

for pet in pets:
    for key, value in pet.items():
        print(f"{key.title()}: {value.title()}")
    print()