#https://www.youtube.com/watch?v=qhnFHnLkrfA
import numpy as np
from numpy.linalg import inv

#Ejercicio 1
P = np.array([[1, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0],
                [0, .1, .1, .8, 0, 0],
                [0, .05, 0, .1, .85, 0],
                [0, .05, 0, 0, .15, .8],
                [.85, .05, 0, 0, 0, .1]])
I = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]) # Identity matrix
O = np.array([[0, 0, 0, 0], [0, 0, 0, 0]]) # Ceros matrix
R = np.array([[0, .1], [0, .05], [0, .05], [.85, .05]])
Q = np.array([[.1, .8, 0, 0], [0, .1, .85, 0], [0, 0, .15, .8], [0, 0, 0, .1]])
F = inv(np.subtract(I, Q))
FR = np.matmul(F, R)
#print(P)
print("Probabilidad de que se gradue: {}".format(FR[0][0]))
print("Probabilidad de que deserte: {}".format(FR[0][1]))
