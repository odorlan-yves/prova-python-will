num = int(input("Digite um número: "))
soma = sum(i for i in range(1, num+1, 2))
print(f"A soma dos números ímpares até {num} é {soma}")
