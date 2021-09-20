alien_0 = {} #também pode ser alien_0 = dict()

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}

print(alien_0['color'])
print(alien_0['points'])

#como chave posso usar numero, string, lista ou outro dicionário

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

del alien_0['points']
#exclui a chave-valor 'points'

favorite_languages = {
    'Michael': 'php',
    'Jim': 'javascript',
    'Pam': 'flutter',
    'Dwight': 'C#',
    'myself': 'Python',
}

print(f"My favorite language is {favorite_languages['myself']}")

loved_person = {
    'first_name': 'Miguel',
    'last_name': 'Albuquerque',
    'age': 4,
    'city': 'Itabaiana'
}

print("My loved person is " + loved_person['first_name']
      + "\nLast name: " + loved_person['last_name']
      + "\nAge: " + str(loved_person['age'])
      + "\nCity: " + loved_person['city'] + ".")
print()

glossary = {
    'print': 'Imprime o valor na tela',
    'string': 'Cadeia de caracteres',
    'float': 'Número flutuante que representa os reais',
    'if': 'Condicional Se... Então',
    'else': 'Condicional Senão...',
}

print("Glossário:" +
      "\n\tPrint: " + glossary['print'] +
      "\n\tString: " + glossary['string'] +
      "\n\tFloat: " + glossary['float'] +
      "\n\tIf: " + glossary['if'] +
      "\n\tElse: " + glossary['else'])