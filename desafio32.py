ano = int(input('Digite um ano: '))
teste = ano / 4
teste = teste.is_integer()
if teste:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))
