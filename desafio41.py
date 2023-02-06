b = '=' * 100
ano = 2023
nasc = int(input('Digite o ano que você nasceu'))
idade = ano - nasc
if idade < 9:
    print('Categoria Mirim')
elif 9 <= idade < 14:
    print('Categoria Infantil')
elif 14 <= idade < 19:
    print('Categoria Junior')
elif 19 <= idade < 20:
    print('Categoria Sênior')
elif idade >= 20:
    print('Categoria Master')
else:
    print('Valor inválido digitado')

