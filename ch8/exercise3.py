dangerous = ['goku', 'roger', 'kuroro', 'laxus', 'luke', 'saga', 'Fox']
rank_s = []

def show_wanted(wanteds):
    """[Mostra o nome de cada procurado da lista]

    Args:
        wanteds (list): [lista com os procurados]
    """
    for wanted in wanteds:
        print(wanted)

def most_wanted(wanteds, worsts):
    """[Transforma uma lista de procurados em mais procurados]

    Args:
        wanteds (list): [Lista de procurados]
        worsts (list): [Lista vazia]
    """
    while wanteds:
        wanted = wanteds.pop()
        worsts.append("The Rank S, most wanted: " + wanted.capitalize())

most_wanted(dangerous[:], rank_s)
show_wanted(dangerous)
print()

show_wanted(rank_s)