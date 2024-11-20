import numpy as np

A = np.array([1, 2, 3])
B = np.array([4, 5, 6])

# Vertikal stacking
C = np.vstack((A, B))

# Horizontal stacking
D = np.hstack((A, B))

print(C)
print(D)
