my_foods = ['pizza', 'tartalete', 'pastel', 'hamburguer']
miguel_foods = my_foods[:]
print(my_foods, miguel_foods)
# copia a lista do primeiro ao último item

my_foods.append('strawberry')
miguel_foods.append('lollipop')
print(my_foods, miguel_foods)

other_person_foods = miguel_foods.copy()
# também serve para copiar uma lista

# miguel_foods = my_foods está errado, pois assim é feito uma linkagem com a lista e nao uma copia