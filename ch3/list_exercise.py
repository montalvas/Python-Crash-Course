guests = ['Barão de Mauá', 'Tesla', 'Leonardo da Vinci']
invitation = 'Seja bem-vindo! sinta-se à vontade Sr. '

for guest in guests:
    print(invitation + guest)
print()

print(f'Infelizmente o Sr. {guests[2]} não poderá participar.')
guests[2] = 'Ada Lovelace'
invitation = 'Seja bem-vindo! sinta-se à vontade Sr(a). '

for guest in guests:
    print(invitation + guest)
print()

guests.insert(0, 'Alan Turing')
guests.insert(1, 'Steve Jobs')
guests.append('Scott Rogers')

for guest in guests:
    print(invitation + guest)
print()

print('Infelizmente a mesa não chegou a tempo, posso convidar apenas duas pessoas.')
while len(guests) != 2:
    uninvited = guests.pop()
    print(f"Desculpe por desconvida-lo Sr(a). {uninvited}")
print()

for guest in guests:
    print(f"Você ainda está convidado Sr.(a) {guest}")
print()

del guests[1]
del guests[0]
print(guests)