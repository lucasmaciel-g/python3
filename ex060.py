#Usando FOR

print("Vamos ver a fatorial de um número!")
n = int(input("Insira um numero: "))
fatorial_for = 1
for i in range(1, n + 1):
    fatorial_for *= i
print(f"O fatorial de {n} é {fatorial_for}.")

#Usando WHILE

fatorial_while = 1
contador = 1
while contador <= n:
    fatorial_while *= contador
    contador += 1
print(f"Fatorial de {n} é {fatorial_while}.")