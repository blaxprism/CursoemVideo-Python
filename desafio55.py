n = []
for c in range(1, 6):
    peso = float(input('Insira o peso da pessoa {}: '.format(c)))
    n.append(peso)
maior = max(n, key=float)
menor = min(n, key=float)
print('O maior valor foi: {:.2f}'.format(maior))
print('O maior valor foi: {:.2f}'.format(menor))
