c = "a"
while c not in "M F N":
    c = input('''Digite a inicial do seu gênero:
    F = Feminino
    M = Masculino
    N = Não-Binário
    ''').strip().upper()
    if c != "F" and c != "M" and c != "N":
        print('Tu é oq?')
if c == "F":
    print("Seu gênero é Feminino")
elif c == "M":
    print("Seu gênero é Masculino")
else:
    print("Seu gênero é não binário")
