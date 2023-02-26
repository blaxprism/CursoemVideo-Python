from random import randrange as rr
vitorias = 0
b = "-=" * 25
while True:
    npc = rr(10)
    print(b)
    jogador = int(input("Digite um número: "))
    print(b)
    opc = int(input("Par(0) ou impar(1)?"))
    soma = npc + jogador
    if soma % 2 == 0 and opc == 0:
        print(b)
        print("Você ganhou!")
        vitorias += 1
    else:
        print(b)
        print("Você perdeu")
        break
print(b)
if vitorias > 1:
    print(f"Você venceu {vitorias} vezes")
elif vitorias == 1:
    print(f'Você venceu {vitorias} vez')
elif vitorias == 0:
    print("Você não venceu nenhuma vez")
else:
    print(f"Como tu venceu vezes negativas:")
print(b)