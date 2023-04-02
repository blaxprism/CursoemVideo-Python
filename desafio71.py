valor = inicial = int(input("Digite o valor a ser sacado: "))
cinquenta = 0
vinte = 0
dez = 0
um = 0

while True:
    if valor >= 50:
        cinquenta += 1
        valor -= 50
    elif valor >= 20:
        vinte += 1
        valor -= 20
    elif valor >= 10:
        dez += 1
        valor -= 10
    elif valor >= 1:
        um += 1
        valor -= 1
    else:
        break

print("==================================================================================")
print(f"O valor inserido foi: {inicial}")
print(f"Foram usadas {cinquenta} notas de R$50.00")
print(f"Foram usadas {vinte} notas de R$20.00")
print(f"Foram usadas {dez} notas de R$10.00")
print(f"Foram usadas {um} moedas de R$1.00")
print("==================================================================================")
