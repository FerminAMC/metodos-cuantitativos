import random

probabilidad_vendido = [.15, .37, .61, .82, 1]
vendidos = [2300, 2400, 2500, 2600, 2700]

# a) Simule las ventas de 10 partidos de futbol
total_a = 0
for i in range(10):
	rand = random.random()
	if(rand <= probabilidad_vendido[0]):
		total_a += vendidos[0] * 1.2
	elif(probabilidad_vendido[0] < rand <= probabilidad_vendido[1]):	
		total_a += vendidos[1] * 1.2
	elif(probabilidad_vendido[1] < rand <= probabilidad_vendido[2]):	
		total_a += vendidos[2] * 1.2	
	elif(probabilidad_vendido[2] < rand <= probabilidad_vendido[3]):	
		total_a += vendidos[3] * 1.2
	elif(probabilidad_vendido[3] < rand <= probabilidad_vendido[4]):	
		total_a += vendidos[4] * 1.2
print("Total ganado en 10 partidos:", total_a)

# b) Simule 10 partidos en el cual se imprimen 2500 programas
total_b = 0
for i in range(10):
	rand = random.random()
	if(rand <= probabilidad_vendido[0]):
		total_b += vendidos[0] * 2
	elif(probabilidad_vendido[0] < rand <= probabilidad_vendido[1]):	
		total_b += vendidos[1] * 2
	elif(probabilidad_vendido[1] < rand <= probabilidad_vendido[2]):	
		total_b += vendidos[2] * 2
print("Total ganado en 10 partidos con 2500 producidos:", total_b - (.8 * 2500))

# c) Simule 10 partidos en el cual se imprimen 2600 programas
total_c = 0
for i in range(10):
	rand = random.random()
	if(rand <= probabilidad_vendido[0]):
		total_c += vendidos[0] * 2
	elif(probabilidad_vendido[0] < rand <= probabilidad_vendido[1]):	
		total_c += vendidos[1] * 2
	elif(probabilidad_vendido[1] < rand <= probabilidad_vendido[2]):	
		total_c += vendidos[2] * 2
	elif(probabilidad_vendido[2] < rand <= probabilidad_vendido[3]):	
		total_c += vendidos[3] * 2

print("Total ganado en 10 partidos con 2600 producidos:", total_c - (.8 * 2500))
