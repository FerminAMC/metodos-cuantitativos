import numpy as np
from numpy.linalg import inv

I = np.array([[1, 0],[0, 1]])
O = np.array([[0, 0], [0, 0]])
A = np.array([[0.6, 0], [0.3, 0.3]])
B = np.array([[0.1, 0.3], [0.2, 0.2]])
F = inv(np.subtract(I, B))
FA = np.matmul(F, A)
M = np.array([50, 30])
MFA = np.matmul(M, FA)
print(MFA)