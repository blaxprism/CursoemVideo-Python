n1 = float(input('Insira um número: '))
n2 = float(input('Insira mais um número: '))
n3 = float(input('Insira mais um número: '))

if n1 > n2:
    if n3 > n1:
        maior = n3
    else:
        maior = n1
else:
    if n3 > n2:
        maior = n3
    else:
        maior = n2
print('O maior valor foi: {}'.format(maior))