from random import choice
n1 = input('Digite o primeiro nome: ')
n2 = input('Digite o segundo nome: ')
n3 = input('Digite o terceiro nome: ')
n4 = input('Digite o quarto nome: ')
list = [n1, n2, n3, n4]  #listas precisam estar entre colchetes#
escolha = choice(list) #apos definir lista eu chamo a função de escolher um item#
print('O nome escolhido para a tarefa foi {}.'.format(escolha))