dias = int(input('Digite a quantidade de dias que você ficou com o carro: '))
km = float(input('Digite quantos km você andou com o carro: '))
pdias = dias*60
pkm = km*0.15
preco = pdias+pkm

print(preco)