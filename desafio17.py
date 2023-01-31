from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
h = hypot(co,ca)
print('''Cateto oposto: {0}
Cateto adjacente: {1}
Hipotenusa: {2}'''.format(co, ca, h))
