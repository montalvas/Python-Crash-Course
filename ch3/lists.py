# O ideal é deixar o nome da lista no plural
# lista são coleções ordenadas

names = ['lucas', 'adriana', 'miguel']
print(names[-1].title()) #Acessa o último elemento da lista

names.append('jojo')
print(names)

colors = []
colors.append('red') #adiciona elemento ao final da lista
colors.append('green')
colors.append('blue')
colors.insert(0, 'RGB') #insere o elemento em determinada posição
print(colors)

breakfast = ['hot dog', 'grape juice']
del breakfast[0] #Apaga o elemento usando o índice, não retorna valor
# Se não especificar o índice, remove toda a lista
juice = breakfast.pop(0) #Apaga o elemento da lista, retorna o valor apagado
print(juice)
#Usar o pop sem especificar o índice faz remover o último elemento da lista

things_to_buy = ['teclado gamer', 'controle gamer', 'roteador', 'monitor']
too_expensive = 'monitor' 
things_to_buy.remove(too_expensive) #remove um elemento pelo valor
print(things_to_buy)
'''
Remove apenas a primeira ocorrência do valor, caso haja mais de um devo usar um loop.
'''
