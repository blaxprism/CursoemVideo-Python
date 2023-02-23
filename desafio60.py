n = int(input('Digite um número: '))
c = n
res = n
while c > 1:
    res = res * (c-1)
    c -= 1
print(res)
