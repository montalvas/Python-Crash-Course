aliens = []

#cria 30 alieniginas e adiciona na lista
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
    
for c in range(0, 5, 1):
    if c % 2 == 0:
        aliens[c]['color'] = 'yellow'
        aliens[c]['points'] = 10
        aliens[c]['speed'] = 'medium'
    elif c % 2 == 1:
        aliens[c]['color'] = 'red'
        aliens[c]['points'] = '15'
        aliens[c]['speed'] = 'fast'

for alien in aliens[:5]:
    print(alien)