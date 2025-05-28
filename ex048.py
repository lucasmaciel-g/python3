s = 0
print("Se prepare, vou calcular todos os numero impares que sao multiplos de 3, no intervalo de 1 a 500. Vamos lá!")
print("Vendo quais são os números no intervalo de 1 a 500...")
print("SAO MUITOS, MEU DEUS!")
print("Agora estou vendo quais sao impares...")
print("Separando os que sao multiplos de 3...")
print("CALCULANDO...")
for i in range(1, 501, 2):
    if i % 3 == 0:
        s += i
print(f"O resultado da soma é {s}.")