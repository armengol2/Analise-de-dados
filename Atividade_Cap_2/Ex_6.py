import math
n = float(input("Insira um numero decimal->"))

print("Raiz quadrada de {}:".format(n), math.sqrt(n))
print("Funcao teto de {}:".format(n), math.ceil(n))
print("Funcao chao de {}:".format(n), math.floor(n))
print("Unidade inteira de {}:".format(n), math.trunc(n))