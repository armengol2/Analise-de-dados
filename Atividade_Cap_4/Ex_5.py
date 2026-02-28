import numpy as np

np.random.seed(10)

arr1 = np.random.randint(1, 51, (4, 4))

print(f"Media linhas= {np.mean(arr1, axis=1)}")
print(f"Media colunas= {np.mean(arr1, axis=0)}")

print(f"Maior media entre linhas= {np.max(np.mean(arr1, axis=1))}")
print(f"Maior media entre colunas= {np.max(np.mean(arr1, axis=0))}")

n, c = np.unique(arr1, return_counts=True)

for num, q in zip(n, c):
    print(f"Numero {num}= {q}")

n2x = n[c == 2]
print(f"Numeros que aparecem 2 vezes={n2x}")