from math import hypot
c1 = float(input('Digite o valor do cateto oposto: '))
c2 = float(input('Digite o valor do cateto adjacente: '))
h = hypot(c1, c2)
print('Se o cateto oposto mede {}, o cateto adjacente mede {}, então a hipotenusa será de {:.2f}.'.format(c1, c2, h))