from random import randint
computador = randint(0, 5)
print("Vamos jogar adivinhação. O computador vai pensar um número de 0 a 5 e você tenta acerta. Vamos lá!")
jogador = int(input("Digite aqui um número de 0 a 5: "))
if jogador == computador:
    print(f"Parábens, o computador também escolher o número {computador}!")
else:
    print(f"O computador escolheu o número {computador}. Uma pena, da próxima vez você tenta novamente")