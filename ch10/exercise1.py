filename = 'ch10/fabula.txt'

with open(filename) as file_object:
    content = file_object.read()
    print(content)