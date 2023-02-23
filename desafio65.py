b = '-=' * 25
n = 0
lista = []
total = 0
mais = 0
while mais != 1:
    print(b)
    n = int(input('Digite um número inteiro: '))
    lista.append(n)
    print(b)
    mais = int(input('Digite 1 para parar de inserir valores: '))
for c in lista:
    total += c
tamanho = len(lista)
media = total/tamanho
maior = max(lista, key=int)
menor = min(lista, key=int)
print(b)
print('Foram digitados {} valores'.format(tamanho))
print(b)
print('A soma dos valores foi de: {}'.format(total))
print(b)
print('A média dos valores foi de: {}'.format(media))
print(b)
print('O maior valor foi: {}'.format(maior))
print(b)
print('O menor valor foi: {}'.format(menor))
print(b)
