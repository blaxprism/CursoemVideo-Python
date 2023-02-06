b = '=' * 100
print(b)
print('Tradutor de caracteres')
print(b)
n = int(input('Digite um número: '))
print(b)
opc = int(input("""Para qual base você gostaria que o número {0} fosse traduzido?
{1}
Digite 0 para Binário 
{1}
Digite 1 para Octal 
{1}
Digite 2 para Hexadecimal
{1}
""".format(n, b)))
print(b)
if opc == 0 or opc == 'Binário' or opc == 'binário' or opc == 'Binario' or opc == 'binario':
    # Pesquisar comandos de formatação para mudar o resultado de "0b10" por exemplo deixando só 10
    print('{} em binário é: {:b}'.format(n, n))
elif opc == 1 or opc == 'Octal' or opc == 'octal':
    print('{} em octal é: {:o}'.format(n, n))
elif opc == 2 or opc == 'Hexadecimal' or opc == 'hexadecimal':
    print('{} em hexadecimal é: {:X}'.format(n, n))
else:
    print('Opção inválida digitada')
print(b)
