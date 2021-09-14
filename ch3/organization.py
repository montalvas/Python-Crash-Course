cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() #Organiza de forma permanente a lista
print(cars)

cars.sort(reverse=True) #Organiza na forma descrente
print(cars)

fruits = ['banana', 'watermelon', 'grape', 'strawberry', 'orange', 'apple']
print(f'Original list: {fruits}')
print(f'Organized list: {sorted(fruits)}')
# Organiza a lista sem altera-la permanentemente

order = ['first', 'second', 'third']
order.reverse()
print(order)
# Apenas inverte permanentemente a ordem dos elementos da lista, não organiza

numbers = [1, 2, 3, 4, 5]
print(len(numbers))
# Tamanho da lista