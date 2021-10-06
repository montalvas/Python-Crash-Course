def get_formatted_location(city, country, population=''):
    """Retorna o nome completo formatado."""
    if population:
        full_location = f'{city}, {country} - população {population}.'
    else:
        full_location = city + ', ' + country
    return full_location.title()