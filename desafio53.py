# replace(" ", "")
# pegar a string
# inverter ela com o for
# testar se ela invertida é igual a ela normal a cada posição
original = input('Digite algo: ')
nospace = original.replace(" ", "").lower()
tamanho = len(nospace)
c2 = 0
teste = 0
for c1 in range(tamanho-1, -1, -1):
    if nospace[c1] != nospace[c2]:
        teste += 1
    c2 += 1
if teste > 0:
    print('Nâo é Palindromo')
elif teste == 0:
    print('É Palindromo')
else:
    print('Erro')
