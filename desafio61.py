print('-=' * 25)
n = int(input('Digite o primeiro termo da PA: '))
print('-=' * 25)
r = int(input('Digite a razão da PA: '))
print('-=' * 25)
c2 = 0
quer = 0
while quer != 1:
    while c2 < 10:
        c2 += 1
        print('Termo {}: {}'.format(c2, n))
        n = n + r
    print('-=' * 25)
    c2 = 0
    quer = int(input('''Deseja exibir mais 10 valores?
    Digite 0 caso queira
    Digite 1 caso não queira
    '''))
    print('-=' * 25)
