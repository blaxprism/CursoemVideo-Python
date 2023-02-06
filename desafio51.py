print('-=' * 25)
n = int(input('Digite o primeiro termo da PA: '))
print('-=' * 25)
r = int(input('Digite a razão da PA: '))
print('-=' * 25)
c2 = 0
for c1 in range(n, n+r*10, r):
    c2 += 1
    print('Termo {}: {}'.format(c2, c1))
print('-=' * 25)
