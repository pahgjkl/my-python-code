import numpy as np
matrix = np.array([
    [85, 90],
    [58, 62],
    [95, 88]
])
print(matrix.shape)
print(matrix.max())
print(matrix.mean(axis=0))