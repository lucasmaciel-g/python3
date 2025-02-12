d = float(input('Qual a cotação do dólar hoje? '))
c = float(input('Qual valor você tem na carteira agora? '))
print('Isso é excelente! Já que você possui R${} na carteira e a cotação está US${} para hoje, você pode comprar US${:.2f}.'.format(c, d, c/d))