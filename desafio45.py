import random
jogo = [0, 1, 2]
valor_pc = random.randrange(0, 3)
jpc = jogo[valor_pc]
valor_jogador = int(input('''Digite sua jogada:
0 = Pedra
1 = Papel
2 = Tesoura\n'''))
if valor_jogador == 0 or valor_jogador == 1 or valor_jogador == 2:
    jj = jogo[valor_jogador]
    if jj == jpc:
        print('Empate')
    elif jj == 0 and jpc == 1:
        print('Voce perdeu, Jogue novamente')
    elif jj == 0 and jpc == 2:
        print('!!! Parabéns, Você venceu !!!')
    elif jj == 1 and jpc == 0:
        print('!!! Parabéns, Você venceu !!!')
    elif jj == 1 and jpc == 2:
        print('Voce perdeu, Jogue novamente')
    elif jj == 2 and jpc == 0:
        print('Voce perdeu, Jogue novamente')
    elif jj == 2 and jpc == 1:
        print('!!! Parabéns, Você venceu !!!')
    else:
        print('Bug Bug Bug')
else:
    print('Valor inválido inserido')
