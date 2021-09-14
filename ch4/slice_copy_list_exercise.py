#copy
languages = ['python', 'php', 'pearl', 'javascript', 'java', 'c#', 'kotlin', 'flutter']

print('The first three languages are:')
for language in languages[:3]:
    print(language)

print('\nThe middle two languages are:')
for language in languages[3:5]:
    print(language)

print('\nThe three final languages are:')
for language in languages[-3:]:
    print(language)

#slice
my_pizzas = ["Atum com catupiry", "Quatro queijos", "Portuguesa"]
wife_pizzas = my_pizzas[:]

my_pizzas.append('Palmito com catupiry')
wife_pizzas.append('Banana com chocolate')

print(f'My favorite pizzas are: {my_pizzas}')
print(f'My wife favorite pizzas are: {wife_pizzas}')