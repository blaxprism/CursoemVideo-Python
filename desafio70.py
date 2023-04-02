compra = {}
n = 20
caros = 0
while True:
    print("==================================================================================")
    produto = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    compra[produto] = preco
    if preco > 1000:
        caros += 1
    while True:
        print("==================================================================================")
        print("Deseja continuar?")
        print("0 - Não")
        print("1 - Sim")
        print("==================================================================================")
        continuar = int(input(""))
        if continuar == 0:
            break
        elif continuar == 1:
            break
    if continuar == 0:
        break
total = sum(compra.values())
preco_mais_barato = min(compra.values())
produto_mais_barato = next(chave for chave, valor in compra.items() if valor == preco_mais_barato)

print("==================================================================================")
print(f"O total gasto na compra foi: {total}")
print(f"{caros} produtos passaram de R$1000,00")
print(f"O produto mais barato foi: {produto_mais_barato} e custou R${preco_mais_barato}")
print("==================================================================================")