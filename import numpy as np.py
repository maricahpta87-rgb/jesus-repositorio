import numpy as np

arr2d = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

# 1. Última columna
print(arr2d[:, 2])

# 2. Dos últimos elementos del array central
print(arr2d[1, 1:])
