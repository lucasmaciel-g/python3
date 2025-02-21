print('Esse programa ajuda a ter uma ideia de investimentos a longo prazo com aportes iguais a cada mês.')

#Entrada de valores

p = float(input('Qual o valor que você pretende colocar nesse investimento mensalmente? '))
i = float(input('Qual a taxa mensal, em porcentagem? '))
a = int(input('Quantos anos você pretende investir? '))

#Calculo do montante investido sem inflação

n = a * 12
m = p * (((1 + (i/100)) ** n - 1) / (i/100))

#Exibição da saida do calculo

print('Desconsiderando a inflação, investindo R${:.2f} ao mês, por {} anos ({} meses), com uma taxa de {}% a.m., você conseguirá R${:.2f}.'.format(p, a, n, i, m))

#Entrada de valor da inflação anual

print('Agora vamos levar em conta a inflação anual que pode existir nesse tempo.')
infan = float(input('Vamos extrapolar a ultima inflação anual para os anos do investimento. Digite aqui a inflação do ultimo ano, em porcentagem: '))

#Calculo do montante considerando a inflação

infmen = ((1 + (infan/100)) ** (1/12)) - 1
mreal = m / ((1 + infmen) ** n)

#Exibição da saida levando em conta a inflação informada

print('Agora, levando em conta a inflação de {:.2f}% a.a. ou {:.4f}% a.m., ao final de {} anos temos um montante de R${:.2f}.'.format(infan, infmen, a, mreal))