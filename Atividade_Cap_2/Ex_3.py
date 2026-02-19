op = (input("Insira uma opcao ="))

while op != "M" and op != "F":
    print("Opcao invalida...")
    op = (input("Insira uma opcao ="))

if op == "M":
    print("Homem")
if op == "F":
    print("Mulher")


