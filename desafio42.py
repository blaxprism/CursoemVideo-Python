b = '=' * 100
print(b)
n1 = float(input('Digite o primeiro número: '))
print(b)
n2 = float(input('Digite o segundo número: '))
print(b)
n3 = float(input('Digite o terceiro número: '))
print(b)
if n3 <= (n1+n2) or n2 <= (n1+n3) or n1 <= (n2+n3):
    print('Triângulo válido ')
    if n1 == n2 == n3:
        print("seu triangulo é equilátero ou seja, tem os 3 lados iguais")
    elif (n1 == n2 != n3) or (n1 != n2 == n3) or (n1 != n3 == n2):
        print("seu triangulo é Isósceles ou seja, tem 2 lados iguais")
    elif n1 != n2 != n3:
        print("seu triangulo é escaleno ou seja, tem os 3 lados diferentes")

else:
    print("Triângulo inválido")
print(b)
