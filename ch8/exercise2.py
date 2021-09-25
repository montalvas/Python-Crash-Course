def city_country(city, country):
    """[Formata o nome da cidade e do país]

    Args:
        city ([str]): [Nome da cidade]
        country ([str]): [Nome do país]

    Returns:
        [str]: [Cidade, País]
    """
    return f"{city.capitalize()}, {country.capitalize()}"

while True:
    cityName = input("Nome da cidade: ")
    countryName = input("Nome do país: ")
    print(city_country(cityName, countryName))
    
    repeat = input("Deseja continuar[S/N]: ")
    if repeat.upper()[0] == "N":
        break