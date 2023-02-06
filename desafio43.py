b = '=' * 100
print(b)
peso = float(input('Insira o seu peso em Quilos: '))
print(b)
altura = float(input('Insira a sua altura em Metros: '))
print(b)
imc = peso / altura**2
if imc < 0:
    imc = imc * (-1)
if imc < 18.5:
    print('Abaixo do peso')
    print("Seu imc é: {:.2f}".format(imc))
elif 18.5 <= imc < 25:
    print('Peso ideal')
    print("Seu imc é: {:.2f}".format(imc))
elif 25 <= imc < 30:
    print('Sobrepeso')
    print("Seu imc é: {:.2f}".format(imc))
elif 30 <= imc < 40:
    print('obesidade')
    print("Seu imc é: {:.2f}".format(imc))
elif imc >= 40:
    print('Obesidade mórbida')
    print("Seu imc é: {:.2f}".format(imc))
else:
    print('valores inválidos inseridos')
print(b)
