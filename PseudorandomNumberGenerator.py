init_seed = 3892
seed = init_seed
a = 16822
c = 12038
results = []
m = pow(2, 32)
for i in range(39999):
    seed = (seed * a + c) % m
    if seed in results:
        break
    results.append(seed)
print(i)
