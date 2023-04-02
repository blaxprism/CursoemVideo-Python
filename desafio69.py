continuar = 1
idade = 0
homens = 0
mulheres = 0
pessoas = 0
while True:
    print("=============================================")
    print("Cadastre uma pessoa")
    print("=============================================")
    while True:
        pessoa = input("Digite seu sexo(F/M): ")
        if pessoa in "fFmM":
            break
    idade = int(input("Digite sua idade: "))
    if pessoa in "fFmM":
        if pessoa in "Mm":
            # Masculino
            homens += 1
        elif (pessoa in "Ff") and idade < 20:
            # Feminino
            mulheres += 1
        if idade > 18:
            pessoas += 1
    else:
        print('Valor inválido inserido')
    while True:
        print("=============================================")
        print("Deseja continuar?")
        print("1 - Sim")
        print("0 - Não")
        print("=============================================")
        continuar = int(input(""))
        if continuar == 0:
            break
        elif continuar == 1:
            break
    if continuar == 0:
        break
print("=============================================")
print(f"{pessoas} pessoas tem mais de 18 anos")
print(f"{homens} homens foram cadastrados")
print(f"{mulheres} mulheres cadastradas tem menos de 20 anos")
print("=============================================")
