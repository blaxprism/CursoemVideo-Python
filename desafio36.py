b = '='*100
print(b)
value = float(input('Digite o valor da casa: '))
print(b)
salario = float(input('Digite seu salário mensal: '))
print(b)
anos = int(input('Digite em quantos anos vai pagar a casa: '))
print(b)
anual = value / anos
mensal = anual / 12
porcento = salario*0.30
if mensal > porcento:
    print('A parcela mensal das parcelas vão exceder 30% do seu salário mensal')
    print('Cada parcela sairá por: R${:.2f}'.format(mensal))
elif mensal == porcento:
    print('A parcela mensal é igual a 30% do seu salário mensal')
    print('Ou seja: {:.2f}'.format(mensal))
elif mensal < porcento:
    print('A parcela mensal é inferior a 30% do seu salário mensal')
    print('Cada parcela sairá por: R${:.2f}'.format(mensal))
else:
    print('Valores inválidos digitados')
print(b)