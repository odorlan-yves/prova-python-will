numeros = [int(input(f"Digite o número {i+1}: ")) for i in range(10)]
pares = [num for num in numeros if num % 2 == 0]
impares = [num for num in numeros if num % 2 != 0]
print(f"Pares: {pares}")
print(f"Ímpares: {impares}")
