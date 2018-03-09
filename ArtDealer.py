import random

runs = 5000
gains_day_1 = 0
gains_day_2 = 0
gains_day_3 = 0

for i in range(runs):
    if(random.random() <= 0.6):
        gains_day_1 += 100000
        if(random.random() <= 0.6):
            gains_day_2 += 200000
            if(random.random() <= 0.6):
                gains_day_3 += 240000

print("Ganancias día 1: ", gains_day_1)
print("Ganancias día 2: ", gains_day_2)
print("Ganancias día 3: ", gains_day_3)
