n1 = float(input('Digite o primeiro número'))
n2 = float(input('Digite o segundo número'))
n3 = float(input('Digite o terceiro número'))

if n3 <= (n1+n2) or n2 <= (n1+n3) or n1 <= (n2+n3):
    print('Triângulo válido')
else:
    print("Triângulo inválido")
