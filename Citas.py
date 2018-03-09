import random

runs = 5000
coincidences = 0
for i in range(runs):
    arrival_afrodicio = 1300 + random.randint(0, 59)
    arrival_rosy = 1300 + random.randint(0, 59)
    range_afrodicio = range(arrival_afrodicio, arrival_afrodicio+20)
    range_rosy = range(arrival_rosy, arrival_rosy+15)
    if (arrival_afrodicio in range_rosy or arrival_rosy in range_afrodicio):
        coincidences += 1
print ("Número de veces que coinciden: ", coincidences)
print ("Probabilidad de que se vean: ", coincidences/runs)
