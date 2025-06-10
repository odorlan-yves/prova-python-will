def soma_multiplos_de_5():
    numeros = []
    while True:
        num = int(input("Digite um número (0 para sair): "))
        if num == 0:
            break
        if num % 5 == 0:
            numeros.append(num)
    print("A soma dos múltiplos de 5 é:", sum(numeros))

soma_multiplos_de_5()
