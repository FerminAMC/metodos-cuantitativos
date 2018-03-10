#https://www.youtube.com/watch?v=qhnFHnLkrfA
import numpy as np
from numpy.linalg import inv
import random

#Ejercicio 1
P1 = np.array([[1, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0],
                [0, .1, .1, .8, 0, 0],
                [0, .05, 0, .1, .85, 0],
                [0, .05, 0, 0, .15, .8],
                [.85, .05, 0, 0, 0, .1]])
I1 = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]) # Identity matrix
O1 = np.array([[0, 0, 0, 0], [0, 0, 0, 0]]) # Ceros matrix
R1 = np.array([[0, .1], [0, .05], [0, .05], [.85, .05]])
Q1 = np.array([[.1, .8, 0, 0], [0, .1, .85, 0], [0, 0, .15, .8], [0, 0, 0, .1]])
F1 = inv(np.subtract(I1, Q1))
FR1 = np.matmul(F1, R1)
print("Ejercicio 1")
print("Probabilidad de que se gradue un alumno de primero: {}".format(FR1[0][0]))
print("Probabilidad de que deserte un alumno de primero: {}".format(FR1[0][1]))


#Ejercicio 2
I2 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
R2 = np.array([[.05, .1, 0, 0, 0, 0], [.02, 0, .2, .5, 0, 0], [.01, 0, 0, 0, .6, .2]])
Q2 = np.array([[.3, .55, 0], [0, .2, .08], [0, 0, .19]])
F2 = inv(np.subtract(I2, Q2))
FR2 = np.matmul(F2, R2)
print("Ejercicio 2")
print("Probabilidad de que un recien nacido muera: {}".format(FR2[0][0]))
ganancia2 = 0
for i in range(1000):
    rand2 = random.random()
    # Venta nivel 1
    if rand2 <= FR2[0][1]:
        ganancia2 += 2000
    elif FR2[0][1] < rand2 <= FR2[0][2]:
        ganancia2 += 3000
    elif FR2[0][2] < rand2 <= FR2[0][3]:
        ganancia2 += 5000
    elif FR2[0][3] < rand2 <= FR2[0][4]:
        ganancia2 += 10000
    elif FR2[0][4] < rand2 <= FR2[0][5]:
        ganancia2 += 20000
print("La ganancia promedio para un animal recien nacido es de {}".format(ganancia2/1000))

#Ejercicio 3
#Empaquetado, Desechado, MA, IA, MB, IB, MC, IC
E =  [1, 0, 0, 0, 0, 0, 0, 0]
D =  [0, 1, 0, 0, 0, 0, 0, 0]
MA = [0, .07, 0, .93, 0, 0, 0, 0]
IA = [0, .02, .04, 0, .94, 0, 0, 0]
MB = [0, .05, 0, 0, 0, .95, 0, 0]
IB = [0, .01, 0, 0, .03, 0, .96, 0]
MC = [0, .03, 0, 0, 0, 0, 0, .97]
IC = [.98, .01, 0, 0, 0, 0, .01, 0]

I3 = np.array([[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1]])
R3 = np.array([[0, .07], [0, .02], [0, .05], [0, .01], [0, .03], [.98, .01]])
Q3 = np.array([[0, .93, 0, 0, 0, 0], [.04, 0, .94, 0, 0, 0], [0, 0, 0, .95, 0, 0],
                [0, 0, .03, 0, .96, 0], [0, 0, 0, 0, 0, .97], [0, 0, 0, 0, .01, 0]])
F3 = inv(np.subtract(I3, Q3))
FR3 = np.matmul(F3, R3)
aux3 = 0
total3 = 0
while aux3 < 1000:
    total3 += 1
    rand3 = random.random()
    if rand3 <= FR3[0][0]:
        aux3 += 1
print("Ejercicio 3")
print("Nececitan entrar {} para que se empaquten 1000".format(total3))
