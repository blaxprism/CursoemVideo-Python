v = float(input('Insira a velocidade do carro: '))
if v > 80:
    multa = (v - 80)*7
    print('O carro foi multado no valor de: R${}'.format(multa))
