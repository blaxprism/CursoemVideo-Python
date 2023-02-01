sal = float(input('Digite seu salário'))
if sal > 1250:
    alm = (sal*0.10)
    novo = sal+alm
    print('o salário foi de {} para {:.2f}, um aumento de {:.2f}'.format(sal, novo, alm))
else:
    alm = (sal * 0.15)
    novo = sal + alm
    print('o salário foi de {} para {:.2f}, um aumento de {:.2f}'.format(sal, novo, alm))
