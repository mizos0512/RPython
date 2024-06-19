import numpy as np

A = np.array([[1, 2, 3, 5],
    [4, 3, 6, 11],
    [2, 0, 6, 11]])

arreglo_lineal = A.reshape(-1)  

print(arreglo_lineal)
