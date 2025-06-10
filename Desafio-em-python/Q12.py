texto = input("Digite um texto: ")
contagem = sum(1 for letra in texto if letra.isalpha())
print(f"O texto tem {contagem} letras")
