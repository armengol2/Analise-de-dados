import numpy as np

arr1 = np.zeros((2, 2))

l = np.random.randint(0, 2)
c = np.random.randint(0, 2)

j = 0
arr1[l, c] = 1

while j < 3:
    coor1 = input("Linha (0 ou 1) -> ")
    while coor1 != "0" and coor1 != "1":
        print("Valor invalido")
        coor1 = input("Linha (0 ou 1) -> ")

    coor2 = input("Coluna (0 ou 1) -> ")
    while coor2 != "0" and coor2 != "1":
        print("Valor invalido")
        coor2 = input("Coluna (0 ou 1) -> ")

    coor1 = int(coor1)
    coor2 = int(coor2)

    if arr1[coor1, coor2] == 1:
        print("Game Over! :( Try Again!")
        j = -1
        break

    j += 1

if j == 3:
    print("Congratulations! You beat the game! :)")