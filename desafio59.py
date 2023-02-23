b = "=-" * 25
c = 4
res = 0
n1 = 0
n2 = 0
while c != 5:
    if c == 1:
        res = n1 + n2
        print(b)
        print('{} + {} = {}'.format(n1, n2, res))
    elif c == 2:
        res = n1 * n2
        print(b)
        print('{} * {} = {}'.format(n1, n2, res))
    elif c == 3:
        maior = max([n1, n2], key=float)
        print(b)
        print('O maior valor foi: {}'.format(maior))
    elif c == 4:
        print(b)
        n1 = float(input('Digite o primeiro número: '))
        print(b)
        n2 = float(input('Digite o segundo número:  '))
    else:
        print(b)
        print('Valor inválido digitado')
    print(b)
    c = int(input('''Digite a opção que desejar
    1 -> Somar os 2 valores
    2 -> Multiplicar os 2 valores
    3 -> Ver qual foi o maior valor inserido
    4 -> Digitar novos números
    5 -> Sair do programa
    '''))
print(b)
