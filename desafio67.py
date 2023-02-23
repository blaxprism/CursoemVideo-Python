b = "-=" * 25
while True:
    print(b)
    n = float(input('Digite um número: '))
    print(b)
    if n < 0:
        break
    c = 1
    while c < 11:
        res = n * c

        print(f"{n} * {c} = {res}")
        c += 1

