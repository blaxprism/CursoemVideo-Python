b = '=' * 100
print(b)
pnormal = float(input('Digite o preço do produto: '))
cpagamento = int(input('''{0}
Condição de pagamento
{0}
Digite 0 para pagar "A vista - Dinheiro/Cheque"
Digite 1 para pagar "A vista - Cartão"
Digite 2 ou mais para pagar parcelado no cartão
{0}
Exemplo: Digite 7 para pagar em sete parcelas no cartão
{0}
'''.format(b)))
print(b)
if pnormal < 0:
    pnormal = pnormal * (-1)

if cpagamento == 0:
    pnovo = pnormal - (pnormal*0.10)
    print('O novo preço é de: R${}'.format(pnovo))
elif cpagamento == 1:
    pnovo = pnormal - (pnormal*0.05)
    print('O novo preço é de: R${}'.format(pnovo))
elif cpagamento == 2:
    print('O Preço é de: R${}'.format(pnormal))
elif cpagamento > 2:
    pnovo = pnormal + (pnormal*0.20)
    print('O novo preço é de: R${}'.format(pnovo))
else:
    print('Valor inválido inserido')
print(b)
