import math

seed = 827364738276364
for j in range(100):
    # Random Number generator
    seed = int(seed)
    seed = pow(seed, 3)
    seed = seed / (math.sqrt(seed))
    seed = math.floor(seed)
    seed = str(seed)
    if(len(seed) % 2 == 0):
        while len(seed) > 16:
            seed = seed[2:]
            seed = seed[:-2]
    else:
        seed = "0" + seed
        while len(seed) > 16:
            seed = seed[2:]
            seed = seed[:-2]
    #print(seed)

    # Valid card verifier
    tarjeta = seed
    nuevo_num = ''
    suma_nuevo_num = 0
    num1 = 0
    num2 = 0
    for i in range(len(tarjeta)):
        if i % 2 == 0:
            if int(tarjeta[i]) * 2 >= 10:
                num1 = 1
                num2 = int(tarjeta[i]) * 2 % 10
                nuevo_num += str(num1 + num2)
            else:
                nuevo_num += str(int(tarjeta[i]) * 2)
        else:
            nuevo_num += tarjeta[i]

    for i in range(len(nuevo_num)):
        suma_nuevo_num += int(nuevo_num[i])

    #print(tarjeta)
    print(suma_nuevo_num % 10 == 0)
