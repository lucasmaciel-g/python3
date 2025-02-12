n = input('Insira seu nome: ')
p = float(input('Qual foi sua nota em português? '))
m = float(input('E qual sua nota em matemática? '))
print('Meu parabéns, {}. Sua nota em português foi {:.2f}, em matemática foi {:.2f}. Isso te garantiu uma média de {:.2f}.'.format(n, p, m, (p+m)/2))