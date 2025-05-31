from random import randint
n1 = randint(0,10)
n2 = randint(0,10)
n3 = randint(0,10)
n4 = randint(0,10)
n5 = randint(0,10)
lista = n1, n2, n3, n4, n5
print(f"Os numeros sorteados foram: {lista}")
print(f"O maior valor é {max(lista)}")
print(f"O menor valor é {min(lista)}")