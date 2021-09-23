responses = {}

polling_active = True # votação ativa

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("\nWhat is your favorite language? ")
    
    responses[name] = response
    # key => name; value => response
    
    repeat = input("Would you like to let another person respond? [yes/no] ")
    
    if repeat == "no":
        polling_active = False

# Mostrar os resultados
print("\n----- Poll Results -----")

for name, response in responses.items():
    print(f"{name} your favorite language is {response}")