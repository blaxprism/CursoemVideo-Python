from random import randrange as rdr
acertou = False
b = "-=" * 50
print(b)
n1 = rdr(0, 11)
while not acertou:
    n2 = int(input('Digite um número de 0 a 10: '))
    print(b)
    if n1 == n2:
        acertou = True
        print('ACERTOOOOOU!!!')
        print('O número que a máquina gerou foi: {}'.format(n1))
    elif n1 > n2:
        print('ERROOOOOUUUU!!!!')
        print('O número que a máquina gerou foi maior que o inserido')
    elif n1 < n2:
        print('ERROOOOOUUUU!!!!')
        print('O número que a máquina gerou foi menor que o inserido')
    print(b)
