op = int(input("numero de pessoas->"))
info = []
soma = 0
cont = 0

for i in range(op):
    print("----------------")
    print("Pessoa", i+1)
    
    nome = input("nome=")
    idade = int(input("idade="))
    sexo = input("sexo=").upper()
    pessoa = {"nome": nome,"idade": idade,"sexo": sexo}
    info.append(pessoa)

    soma += idade

    if sexo == "F":
        cont += 1

media = soma / op

print("Media das idades->", media)
print("Quantidade de F:", cont)