import numpy as np
from numpy.linalg import inv

#quedan, pasan, desertan, mueren
n1 = [.1, .79, .1, .01]
n2 = [.1, .83, .05, .02]
n3 = [.15, .77, .05, .03]
n4 = [.1, .81, .05, .04]

I = np.array([[.1, .79], [.1, .83]])
O = np.array([[.1, .01], [.05, .02]])
A = np.array([[.15, .77], [.1, .81]])
B = np.array([[.05, .03], [.05, .04]])
F = inv(np.subtract(I, B))
FA = np.matmul(F, A)
print(FA)
