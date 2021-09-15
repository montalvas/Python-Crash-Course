#tupla é uma lista imutável
retangle_dimension = (200, 50)
print(f'Dimensoes: {retangle_dimension[0]}x{retangle_dimension[1]}')

buffet = 'Frango Parmegiana', 'Medalhao Chambord', 'Salmao ao molho de maracuja', 'Frango Kiev', 'Salada de camaroes'

for prato in buffet:
    print(prato)

print()
buffet = 'frango caipira', 'boi assado', 'lombo', 'carne de porco', 'toscana'
#posso realocar outra tupla na variável
for prato in buffet:
    print(prato)