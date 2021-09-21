rios = {
    'Amarelo': 'China',
    'Volga': 'Rússia',
    'Tigre': 'Turquia'
}

for rio, pais in rios.items():
    print(f"O rio {rio} corre pela {pais}")
print()

for rio in rios.keys():
    print(f'Rio {rio}')
print()

for pais in rios.values():
    print(f'País {pais}')