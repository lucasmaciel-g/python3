n = int(input("Insira um valor, se quiser encerrar, digite 999: "))

# O programa verifica antes se foi colocado o numero 999

contador = 0
soma = 0

# No while abaixo, se o 999 foi inserido la em cima, ele nem entra no loop.

while n != 999:
    soma += n 
    contador += 1
    n = int(input("Insira um valor, se quiser encerrar, digite 999: "))
print(f"Você inseriu {contador} números e a soma deles foi {soma}.")