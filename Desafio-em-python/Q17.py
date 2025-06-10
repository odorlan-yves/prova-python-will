def par_ou_impar(num):
    return "Par" if num % 2 == 0 else "Ímpar"

num = int(input("Digite um número: "))
print(f"O número {num} é {par_ou_impar(num)}.")
