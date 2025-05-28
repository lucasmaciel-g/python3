frase = input("Digite uma frase para verificar se é um palíndromo: ")
frase_sem_espacos = ""

# Removendo os espaços da frase
for letra in frase:
    if letra != " ":
        frase_sem_espacos += letra

# Invertendo a frase manualmente
frase_invertida = ""
for i in range(len(frase_sem_espacos) - 1, -1, -1):
    frase_invertida += frase_sem_espacos[i]

# Verificando se é palíndromo
if frase_sem_espacos.lower() == frase_invertida.lower():
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")
