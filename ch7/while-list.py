unconfirmed_users = ['logan', 'drake', 'aaron']

confirmed_users = []

while unconfirmed_users: #enquanto a lista não estiver vazia (True)
    current_user = unconfirmed_users.pop()
    #remove o último usuário e retorna para uma variável
    
    print(f"Verifying user: {current_user.capitalize()}")
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:\n") #Os usuários a seguir foram confirmados
for confirmed_user in confirmed_users:
    print(confirmed_user.capitalize())