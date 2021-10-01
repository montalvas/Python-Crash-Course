filename = "ch10\programming.txt"

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I want to be a great programmer.\n")

#Concatenando novas informações (append)
with open(filename, 'a') as file_object:
    file_object.write("May i construct some career and became famous.\n")
    file_object.write("Make a lot of money.\n")
    file_object.write("Be an important person to the world.\n")
    
#Condição para abrir um arquivo

document_path = "ch10/arquivo_teste.txt"
try:
	document_file = open(document_path)
except FileNotFoundError:
	document_file = open(document_path, 'w')