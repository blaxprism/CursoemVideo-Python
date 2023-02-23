quant = int(input('Digite a quantidade de números a ser exibida: '))
n1 = 0
n2 = 1
n3 = n2 + n1
c1 = 0
c2 = 0
while c1 < quant:
    c1 += 1
    c2 += 1
    if c2 <= quant:
        print("Número {}: {}".format(c2, n1))
    c2 += 1
    if c2 <= quant:
        print("Número {}: {}".format(c2, n2))
    c2 += 1
    if c2 <= quant:
        print("Número {}: {}".format(c2, n3))
    n1 = n2 + n3
    n2 = n1 + n3
    n3 = n1 + n2
