from math import sin, cos, tan, radians
a = (float(input('Digite o ângulo qualquer: ')))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))
print('Para o angulo de {} teremos: \nSeno = {:.2f} \nCosseno = {:.2} \nTangente = {:.2f}'.format(a, s, c, t))