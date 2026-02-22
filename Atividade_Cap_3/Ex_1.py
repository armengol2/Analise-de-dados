time = ["Palmeiras", "Barcelona", "Pousao", "flamengo", "esquina juniors"]

print("Podio ->", time[:3])
print("Perdedores ->", time[-2:])
print("Em ordem alfabetica->", sorted(time))
pos = time.index("Barcelona") + 1
print("O barcelona esta em", pos, "° Lugar")