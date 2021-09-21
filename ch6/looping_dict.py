#percorrendo um dicionário

user_admin = {
    'username': 'montalvas',
    'first_name': 'Lucas',
    'last_name': 'Montalvani'
}

for k, v in user_admin.items():
    print(k + ": " + v)
print()

'''
método .keys() percorre somente as chaves do array, retorna um dict com as chaves
método .values() percorre somente os valores, retorna um dict com os valores
método .items() percorre chave e valor, retorna um dict completo
'''

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(" Hi " + name.title() +
        ", I see your favorite language is " +
        favorite_languages[name].title() + "!")

if 'Mikael' not in favorite_languages.keys():
    print("\nMikael, please take our poll!\n")
    
#percorrer um dicionário de forma ordenada:
for person in sorted(favorite_languages.keys()):
    print(f"{person.title()}, thank you for taking the poll.")
print()

#percorrendo os valores do dicionário:
for language in favorite_languages.values():
    print(f"{language.title()} is a program language.")
print()

#criando uma lista sem repetições (conjunto/set):
colors = {
    'John': 'Blue',
    'Deborah': 'Red',
    'Seth': 'Blue',
    'Donald': 'Yellow',
    'Armin': 'Red'
}

print(set(colors.values()))
#No set não há repetição de valores