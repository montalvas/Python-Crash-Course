'''
prompt = "\nQual ingrediente gostaria de adicionar na pizza?"
prompt += "\nDigite 'quit' para sair. "

while True:
    ingrediente = input(prompt)
    if ingrediente == 'quit':
        break
    else:
        print(f"{ingrediente.capitalize()} foi adicionado na pizza!")
'''

atender_cliente = True
valor_total = 0
ingresso = 0

while atender_cliente:
    comprar_ingresso = input("Gostaria de comprar um ingresso? [S/N] ").upper()[0]
    
    if comprar_ingresso == "S":
        idade_pessoa = int(input("\nQual a sua idade: "))
        
        if idade_pessoa < 0:
            print("Idade inválida.\n")
        elif idade_pessoa < 3:
            print("Seu ingresso será gratuito.\n")
            ingresso += 1
        elif idade_pessoa < 13:
            print("Seu ingresso custa R$ 10,00.\n")
            ingresso += 1
            valor_total += 10
        elif idade_pessoa < 140:
            print("Seu ingresso custa R$ 15,00.\n")
            ingresso += 1
            valor_total += 15
        else:
            print("Idade inválida.\n")
    elif comprar_ingresso == "N":
        if ingresso != 0:
            print(f"Você comprou {ingresso} ingresso(s).")
            print("Total R$ {:.2f}".format(valor_total))
        print("\nObrigado e volte sempre!")
        atender_cliente = False
    else:
        print("Opção inválida.\n")  