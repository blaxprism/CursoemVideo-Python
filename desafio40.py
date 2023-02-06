b = '=' * 100
print(b)
n1 = float(input('Digite a nota 1: '))
print(b)
n2 = float(input('Digite a nota 2: '))
print(b)
media = (n1+n2)/2
if media < 5:
    print('A sua média é: {} \nVocê foi reprovado'.format(media))
elif 5 <= media < 7:
    print('A sua média é: {} \nVocê está de recuperação'.format(media))
elif media >= 7:
    print('A sua média é: {} \nVocê foi aprovado'.format(media))
else:
    print('Valores inválidos inseridos')
print(b)
