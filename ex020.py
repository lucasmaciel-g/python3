from random import shuffle
n1 = str(input('Digite o nome de um aluno: '))
n2 = str(input('digite o nome de outro: '))
n3 = str(input('Digite outro nome: '))
n4 = str(input('Digite o nome do último: '))
deck = [n1, n2, n3, n4] #precisa criar lista
shuffle(deck)
print(deck)
