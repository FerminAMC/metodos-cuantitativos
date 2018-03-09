import numpy as np
import random

# Didn't know if i had to keep the the 3 by 3 matrix random or fixed, so I kept it fixed
# and only did the 1 by 3 matrix random every time
a1 = random.random()
b1 = random.random()
c1 = random.random()
denom1 = a1 + b1 + c1
a2 = random.random()
b2 = random.random()
c2 = random.random()
denom2 = a2 + b2 + c2
a3 = random.random()
b3 = random.random()
c3 = random.random()
denom3 = a3 + b3 + c3
y = [[a1/denom1, b1/denom1, c1/denom1], [a2/denom2, b2/denom2, c2/denom2], [a3/denom3, b3/denom3, c3/denom3]]

runs = 5000
counter_total = []

#NOTE: for some reason the program sometimes gets stuck in the wile loop. Just run it again...
for i in range(runs):
    a = random.random()
    b = random.random()
    c = random.random()
    denom = a + b + c
    x = [a/denom, b/denom, c/denom]

    x = np.array(x)
    y = np.array(y)

    counter = 0
    aux = 0
    while(aux == 0 or counter > 200):
        counter += 1
        resp = np.matmul(x, y)
        if (np.array_equal(x, resp)):
            aux = 1
            counter_total.append(counter)
        else:
            x = resp

print("Average runs:", sum(counter_total)/runs)
