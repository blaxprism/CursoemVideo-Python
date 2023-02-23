n = 0
lista = []
res = 0
while n != 999:
    n = int(input('Digite um número inteiro: '))
    if n != 999:
        lista.append(n)
for c in lista:
    res += c
tamanho = len(lista)
print('Foram digitados {} valores(fora o 999)'.format(tamanho))
print('A soma dos valores foi de: {}'.format(res))
