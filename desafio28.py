from random import randrange as rdr
n1 = rdr(1, 6)
n2 = int(input('Digite um número de 1 a 5: '))
if n1 == n2:
    print('ACERTOOOOOU!!!')
    print('O número que a máquina gerou foi: {}'.format(n1))
else:
    print('ERROOOOOUUUU!!!!')
    print('O número que a máquina gerou foi: {}'.format(n1))
    print('O número que você digitou foi: {}'.format(n2))
