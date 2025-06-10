num = int(input("Digite um número: "))
primo = num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))
print(f"O número {num} {'é' if primo else 'não é'} primo")
