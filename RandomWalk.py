import random

# n is the number of blocks you can advance
def random_walk(n):
    x = 0
    y = 0      # North   South   East    West
    direction = [(0,1), (0,-1), (1, 0), (-1,0)]
    for i in range(n):
        # Picks between N, S, E, W randomly
        (dx, dy) = random.choice(direction)
        x += dx
        y += dy
    return (x, y)
# Number of times the program will try the Random Walk
number_of_tries = 15
# Number of blocks walked
number_of_blocks = 10
# Number of times the program ends with a distance equal or lower than the acceptance value
passes = 0
# Distance accepted as a pass by the program
acceptance = 2
for i in range(number_of_tries):
    walk = random_walk(number_of_blocks)
    distance = abs(walk[0]) + abs(walk[1])
    if(distance <= acceptance):
        print "Distance from the bar =" , distance, "<PASS>"
        passes += 1
    else:
        print "Distance from the bar =" , distance, "<FAIL>"
        #passes += 0
chance_of_passing = float(passes) / number_of_tries
print "-----------------------------------------------------------"
print "| Chance of ending 2 blocks or less away from bar = ", chance_of_passing , "|"
print "-----------------------------------------------------------"
