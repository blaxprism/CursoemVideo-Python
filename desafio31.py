km = float(input('Insira a distância da viagem em Km: '))
if -200 <= km <= 200:
    conta = 0.50*km
    print(conta)
else:
    conta = 0.45*km
    print(conta)
