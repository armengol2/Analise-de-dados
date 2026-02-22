nome1 = input("pessoa 1->")
peso1 = float(input("Peso 1->"))
info1 = {"nome": nome1, "peso": peso1}
nome2 = input("pessoa 2->")
peso2 = float(input("Peso 2->"))
info2 = {"nome": nome2, "peso": peso2}
nome3 = input("pessoa 3->")
peso3 = float(input("Peso 3 ->"))
info3 = {"nome": nome3, "peso": peso3}

p = [info1, info2, info3]

mais = p[0]
menos = p[0]

for pessoa in p:
    if pessoa["peso"] > mais["peso"]:
        mais = pessoa
        
    if pessoa["peso"] < menos["peso"]:
        menos = pessoa

print("Pessoa mais pesada:", mais["nome"])
print("Pessoa mais leve:", menos["nome"])