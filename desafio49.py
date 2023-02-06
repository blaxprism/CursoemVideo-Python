print('-=' * 25)
n = int(input('Digite um número: '))
for c in range(1, 11):
    print('-=' * 25)
    print('{} * {} = {}'.format(n, c, n*c))
print('-=' * 25)