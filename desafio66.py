todos = []
b = "-=" * 25
while True:
    print(b)
    num = int(input("Digite um número: "))
    if num == 999:
        break
    todos.append(num)
soma = sum(todos)
quantidade = len(todos)
print(b)
print(f"A soma de todos os valores resultou em: {soma}")
print(b)
print(f"Foram digitados {quantidade} valores")
print(b)
