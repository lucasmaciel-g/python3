s = 0
print("Insira seis numero que vou somar os pares e te retornar o valor da soma!")
for i in range(0, 6):
    n = int(input("Digite um valor: "))
    if n % 2 == 0:
        s += n
print(f"A soma valores pares foi {s}.")