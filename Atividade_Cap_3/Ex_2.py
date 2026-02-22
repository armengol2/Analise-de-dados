l1 = {"Iphone 13", "Iphone 15", "Xiaomi 12", "Motorola Edge"}
l2 = {"Iphone 15", "Iphone 7", "Samsumg 23 fe", "Galaxy j1 mini"}

m1 = l1 | l2
m2 = l1 & l2

print("Disponiveis nas loja->", m1)
print("Disponiveis em ambas->", m2)