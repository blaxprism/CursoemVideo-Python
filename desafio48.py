soma = 0
for c in range(0, 501, +3):
    teste = c % 2
    if teste == 1:
        soma += c

print('-=' * 25)
print('A soma resultou em: {}'. format(soma))
print('-=' * 25)