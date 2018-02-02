import numpy as np
# np.random.normal(mean, std, size) returns array[size] of normal distribution
total_hours_a = 20000
total_hours_b = 20000

class Component:
    def __init__(self, life_time):
        self.life_time = life_time

Components_a = []
Components_b = []
cost_a = 0
cost_b = 0

# All four components are added to the array
Components_a.append(Component(np.random.normal(600, 100)))
Components_a.append(Component(np.random.normal(600, 100)))
Components_a.append(Component(np.random.normal(600, 100)))
Components_a.append(Component(np.random.normal(600, 100)))

Components_b.append(Component(np.random.normal(600, 100)))
Components_b.append(Component(np.random.normal(600, 100)))
Components_b.append(Component(np.random.normal(600, 100)))
Components_b.append(Component(np.random.normal(600, 100)))

# a) Components are changed individually as they deteriorate
while (total_hours_a > 0):
    total_hours_a -= 1
    for j in range(len(Components_a)):
        Components_a[j].life_time -= 1
        if(Components_a[j].life_time <= 0):
            cost_a += 300 # $200 for the replacement part and $100 for the downtime of the equipment
            total_hours_a -= 1
            Components_a[j].life_time = np.random.normal(600, 100)

print ("Cost a: ", cost_a)

# b) All components are changed when one deteriorates in order to reduce downtime
while (total_hours_b > 0):
    total_hours_b -= 1
    j = 0
    while (j < len(Components_b)):
        Components_b[j].life_time -= 1
        if (Components_b[j].life_time <= 0):
            cost_b += 1000 # $200 for each replacement part (4) and $200 for the downtime of the equipment
            total_hours_b -= 2
            Components_b[0].life_time = np.random.normal(600,100)
            Components_b[1].life_time = np.random.normal(600,100)
            Components_b[2].life_time = np.random.normal(600,100)
            Components_b[3].life_time = np.random.normal(600,100)
            j = 3
        j += 1

print ("Cost b: ", cost_b)

#NOTE: There is almost no difference between any of the methods. One tends to be marginally more expensive than the other at random
