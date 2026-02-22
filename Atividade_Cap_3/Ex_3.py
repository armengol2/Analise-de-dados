nome = str(input("nome do aluno ="))
nota1 = int(input("Nota da prova 1 ="))
nota2 = int(input("Nota da prova 2 ="))

media = (nota1 + nota2)/2

if media >= 50:
    op = "AP"
else:
    op = "RP"

info = {"Nome": nome,"Nota 1": nota1,"Nota 2": nota2,"Media": media,"Situacao": op}

print(info.values())