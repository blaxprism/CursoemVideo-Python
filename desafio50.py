soma = 0
for c in range(0, 6):
    n = int(input('Digite um número: '))
    teste = n % 2
    if teste == 0:
        soma += n
print('-=' * 25)
print('A soma resultou em: {}'. format(soma))
print('-=' * 25)
