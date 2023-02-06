b = '=' * 100
print(b)
n1 = int(input('Digite um número: '))
print(b)
n2 = int(input('Digite mais número: '))
print(b)
if n1 > n2:
    print('{} é maior que {}'.format(n1, n2))
elif n2 > n1:
    print('{} é maior que {}'.format(n2, n1))
elif n1 == n2:
    print('{} é igual a {}'.format(n1, n2))
else:
    print('Valor inválido inserido')
print(b)