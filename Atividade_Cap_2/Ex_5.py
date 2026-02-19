n = int(input("Numero entre 1000 e 9999->"))

print("unidade de {}:".format(n), n % 10)
print("dezena de {}:".format(n), (n // 10) % 10)
print("centena de {}:".format(n), (n // 100) % 10)
print("milhar de {}:".format(n), n // 1000)