from random import randint
print("Vamos jogar adivinhação. O computador vai pensar um número de 1 a 10 e você tenta acerta. Vamos lá!")
computador = randint(1, 10)
tentativa = 0
jogador = 15
while jogador != computador:
    jogador = int(input("Digite aqui um número de 1 a 10: "))
    tentativa += 1
    print(f"O número {jogador} ainda não é o certo.")
print(f"Parabéns, o computador escolheu {computador} e você precisou de {tentativa} tentativas para acertar.")