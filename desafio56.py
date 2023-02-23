b = '-=' * 50
d = '=-' * 50
soma_idades = 0
velho_idade = 0
mulheres = 0
velho_nome = "Nenhum, não tem nenhum homem"
nb = 0
print(b)
for c in range(1, 5):
    nome = input('Digite o nome da {} pessoa: '.format(c))
    print(b)
    idade = int(input('Digite a idade da {} pessoa: '.format(c)))
    print(b)
    genero = int(input('''Digite o gênero da {} pessoa: 
    0 = Mulher
    1 = Homem
    2 = Não binário
    '''.format(c)))
    print(b)
    print(d)
    soma_idades += idade
    if genero == 1 and idade > velho_idade:
        velho_idade = idade
        velho_nome = nome
    if genero == 0 and idade < 20:
        mulheres += 1
    if genero == 2:
        nb += 1
media = soma_idades / 4
print('A Média das idades de todas as pessoas foi: {:.2f}'.format(media))
print(b)
print('O nome do homem mais velho foi: {}'.format(velho_nome))
print(b)
print('A quantidade de mulheres com menos de 20 anos foi: {}'.format(mulheres))
print(b)
print('A quantidade de pessoas não binárias foi: {}'.format(nb))
