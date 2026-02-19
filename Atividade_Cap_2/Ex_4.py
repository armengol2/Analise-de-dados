d = float(input("Insira a distancia->"))

if d <= 200:
    print("Viagem de {} KM por R$".format(d), d * 0.5)
else:
    print("Viagem de {} KM por R$".format(d), d * 0.45)