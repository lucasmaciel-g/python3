k = (float(input('Quantos quilometros você rodou com o carro? ')) * 0.15)
d = (int(input('Quantos dias o carro ficou com você? ')) * 60)
print('Com base nos dados inserido, o valor total do aluguel será de R${:.2f}.'.format(k + d))
