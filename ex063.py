n = int(input("digite um numero: "))
a = 0
b = 1
contador = 0
while contador < n:
    print(a)
    proximo = a + b
    a = b
    b = proximo
    contador += 1
print("FIM")
