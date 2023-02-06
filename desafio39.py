anoatual = 2023
nasc = int(input('Digite o ano que você nasceu: '))
idade = anoatual - nasc
diferenca = idade - 18

if idade < 18:
    diferenca = diferenca * (-1)
    print('Você ainda vai se alistar')
    print('falta {} ano(s)'.format(diferenca))
elif idade == 18:
    print('Esse é o ano do seu alistamento')
elif idade > 18:
    print('Você já se alistou ou deveria ter se alistado')
    print('passou {} ano(s) do seu alistamento'.format(diferenca))
else:
    print('Valor inválido inserido')
