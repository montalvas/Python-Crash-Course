#Uma forma de armazenar dados é usando JSON (formato universal)
import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as file_object:
    json.dump(numbers, file_object)
    #armazena a lista no arquivo criado
    