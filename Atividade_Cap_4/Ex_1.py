import numpy as np

arr1 = np.array([1,1,1,1,1,1,1,1])
arr2 = np.random.randint(1, 10, 8)

arr3 = (arr1 + arr2)

soma = arr3.sum()

if soma >= 40:
    print(arr3.reshape(4,2))
else:
    print(arr3.reshape(2,4))
