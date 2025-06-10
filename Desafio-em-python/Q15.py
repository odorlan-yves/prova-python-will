def maior_valor():
    numeros = [int(input(f"Digite o {i+1}º número: ")) for i in range(5)]
    print("O maior número é:", max(numeros))

maior_valor()
