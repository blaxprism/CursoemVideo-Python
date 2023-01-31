from math import radians, sin, cos, tan
n = float(input('Digite a medida em graus: '))
n = radians(n)
sn = sin(n)
cs = cos(n)
tg = tan(n)

print('''Medidas em radianos:
O Seno é de {:.2f}
O Cosseno é de {:.2f}
A Tangente é de {:.2f}
'''.format(sn, cs, tg))