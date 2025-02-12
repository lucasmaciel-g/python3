c = float(input('Qual o comprimento da parede a ser pintada, em metros? '))
a = float(input('E qual a altura, em metros? '))
print('Sua parede tem {:.2f} m2. Sabemos que cada litro de tinta pinta 2 m2. Dito isso, você vai gastar {:.1f} L de tinta nessa parede.'.format((c*a), (c*a)/2))