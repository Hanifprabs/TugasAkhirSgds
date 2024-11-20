import numpy as np

A = np.array([[1, 2], [3, 4]])

# Invers matriks
inverse_A = np.linalg.inv(A)

# Determinan matriks
det_A = np.linalg.det(A)

print(inverse_A)
print(det_A)
