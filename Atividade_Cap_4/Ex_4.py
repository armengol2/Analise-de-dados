import numpy as np

arr1 = np.array([[1, 2, 3], [5, 6, 7], [9, 10, 11]])

l, c = arr1.shape

total = l * c

if total % 2 == 0:
    print("Vetor par")

else:
    print("Vetor impar")
