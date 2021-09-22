cities = {
    'Brisbane': {
      'country': 'Australia',
      'population': '2.28 milhões',
      'fact': 'A área cultural de South Bank reúne o Museu de Queensland e o Sciencentre, com exposições interativas importantes.',
    },
    'Winnipeg': {
        'country': 'Canada',
        'population': '749.534',
        'fact': 'Seu centro é The Forks, um local histórico na interseção entre os rios Red e Assiniboine, com depósitos transformados em lojas e restaurantes, além da ampla área verde dedicada a festivais, shows e exposições.',
    },
    'Lisboa': {
        'country': 'Portugal',
        'population': '504.718',
        'fact': 'Do imponente Castelo de São Jorge, a vista abrange as construções em tons pastel da cidade antiga, o estuário do Tejo e a Ponte 25 de Abril. Perto dali, o Museu Nacional do Azulejo exibe 5 séculos de azulejos decorativos.',
    }
}

for city, info in cities.items():
    print(f"City:")
    print(f"\tAbout {city}: City from {info['country']}. Has {info['population']} inhabitants. {info['fact']}")
    print()