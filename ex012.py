p1 = float(input('Qual o valor original do produto? R$'))
d = float(input('Qual o desconto voce quer dar (insira o numero fracionado)? '))
print('Se o valor original era R${}, e voce quer dar um desconto de {}%, o novo valor sera de R${:.2f}.'.format(p1, d*100, p1*(1-d)))