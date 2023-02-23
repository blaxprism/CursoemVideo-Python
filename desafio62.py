print('-=' * 25)
n = int(input('Digite o primeiro termo da PA: '))
print('-=' * 25)
r = int(input('Digite a razão da PA: '))
print('-=' * 25)
c2 = 0
quer = 10
quant = 10
while quer > 0:
    while c2 < quant:
        c2 += 1
        print('Termo {}: {}'.format(c2, n))
        n = n + r
    print('-=' * 25)
    quer = int(input('Deseja exibir mais quantos termos?: '))
    quant = quer+c2
    print('-=' * 25)
