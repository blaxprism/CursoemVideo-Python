ano = 2023
maioridade = 0
menoridade = 0
b = '-=' * 25
print(b)
for c in range(1, 8):
    nascimento = int(input('Digite o ano de nascimento da pessoa {}: '.format(c)))
    idade = ano - nascimento
    print(b)
    if idade >= 21:
        maioridade += 1
    else:
        menoridade += 1
print('{} pessoas atingiram a maioridade'.format(maioridade))
print(b)
print('{} pessoas ainda vão atingir a maioridade'.format(menoridade))
print(b)
