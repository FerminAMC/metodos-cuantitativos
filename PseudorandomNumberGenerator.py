init_seed = 3892
seed = init_seed
a = 168223
c = 120383
results = []
m = pow(2, 32)
for i in range(10000):
    seed = (seed * a + c) % m
    if seed in results:
        break
    results.append(seed)
    # Uncomment this to visualize the auto generated seeds
    #print(seed)
print(i)
