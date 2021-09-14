string = "My name is Lucas"
string_lower_case = string.lower() #Toda minúscula
string_upper_case = string.upper() #Toda maiúscula

print(string, string_lower_case, string_upper_case)

first_programmer = "ada lovelace"
print(first_programmer.title()) #Primeira maiúscula e demais minúsculas

first_name = "miguel"
second_name = "montalvani"
full_name = first_name + " " + second_name #concatenação
print(f"My son name is {full_name.title()}")

print("\tPython") #imprime com identação (tab)

print("blank space in right           ".rstrip()) #Elimina os espaços em branco à direita
print("     blank space in left".lstrip()) #Elimina os espaços em branco à esquerda
print("     blank space in center     ".strip()) #Elimina os espaços em branco nos dois lados
# Se quiser manter devo armazenar na variável, senão será temporário

famous_person = "Alan Turing"
message = famous_person + " " + "certa vez disse: 'Nós só podemos ver um pouco do futuro, mas o suficiente para perceber que há muito a fazer.'"
print(message)

lucky_number = 5
print("My lucky number is " + str(lucky_number))