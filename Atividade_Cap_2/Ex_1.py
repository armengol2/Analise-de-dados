nome = str(input())
print("maiusculo = ", nome.upper())
print("minusculo = ", nome.lower())
print("contagem = ", len(nome))
partes = nome.split()
ultimo = partes[-1]
nome2 = nome.replace(ultimo, "do inatel")
print("trocar = ", nome2)