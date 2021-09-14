players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
# fatia do index 0 ao 2

print(players[:4])
#sem o índice de início, ele pega o primeiro elemento da lista

print(players[2:])
#sem o índice do final, ele vai até o último elemento da lista

print(players[-2:])
#exibe os 3 últimos jogadores da lista

#posso combinar com o for para percorrer um subconjunto de lista
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())