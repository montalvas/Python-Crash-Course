print("Soma entre dois números")
while True:
    try:
        first_number = int(input("Digite o primeiro número: "))
        second_number = int(input("Digite o segundo número: "))
    except (ValueError, TypeError):
        print("Valor inválido.")
    else:
        result = first_number + second_number
        print(f"Resultado é {result}")
        break