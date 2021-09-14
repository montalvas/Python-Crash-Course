#criar lista usando range
numbers = list(range(1, 6))
print(numbers)

#pares entre 1 e 10
even_numbers = list(range(2, 11, 2))
print(even_numbers)

#ímpares entre 1 e 10
odd_numbers = list(range(1, 10, 2))
print(odd_numbers)

#lista com os 10 primeiros quadrados perfeitos
squares = list()
for number in range(1, 11):
    squares.append(number ** 2)
print(squares)

#valor mínimo, máximo e a soma dos valores de uma lista
random_numbers = [3, 7, 4, 8, 9, 0, 2, 1, 5]
print(f"Valor minimo da lista: {min(random_numbers)}")
print(f"Valor maximo da lista: {max(random_numbers)}")
print(f"Soma dos valores da lista: {sum(random_numbers)}")

multiples = list(range(3, 31, 3))
print(f"Multiplos de 3: {multiples}")