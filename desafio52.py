print('-='*50)
n = int(input('Digite o número que gostaria de testar: '))
print('-='*50)
primo = "é primo"
if n > 3:
    for c in range(2, n-1):
        if n % c == 0:
            primo = "Não é Primo"
    print("O número {} {}".format(n, primo))
elif n == 2:
    primo = "é Primo"
    print("O número {} {}".format(n, primo))
elif n == 3:
    primo = "é Primo"
    print("O número {} {}".format(n, primo))
else:
    print('Erro')
print('-='*50)
