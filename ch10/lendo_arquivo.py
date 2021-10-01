with open('ch10/pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents, end="\n\n")

file_path = "C:/Users/lucas/OneDrive/Documentos/document.txt"
with open(file_path) as file_object:
   for line in file_object:
       print(line.rstrip())
       
filename = 'ch10/poema.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

print()
for line in lines:
    print(line.rstrip())