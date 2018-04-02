import random
# a) Simule 15 días de descarga de barcazas y calcule el número promedio de barcazas retrasadas, el número promedio de llegadas por día y el número promedio de barcazas descargadas
probabilidad_descarga = [.03, .15, .55, .83, .95, 1]
numero_descargas = [1, 2, 3, 4, 5, 6]
# Las probabilidades de llegada las tomé de una actividad pasada similar a esta
probabilidad_llegada = [.13, .3, .45, .7, .9, 1]
numero_llegadas = [0, 1, 2, 3, 4, 5]  

llegadas_totales = 0
atendidos_totales = 0
retrasos_totales = 0
restantes = 0

for i in range(15):
	rand_1 = random.random()
	rand_2 = random.random()
	# Llegadas del día
	llegadas = 0 + restantes
	if(rand_1 <= probabilidad_llegada[0]):
		llegadas_totales += numero_llegadas[0]
		llegadas += numero_llegadas[0]
	elif(probabilidad_llegada[0] < rand_1 <= probabilidad_llegada[1]):
		llegadas_totales += numero_llegadas[1]
		llegadas += numero_llegadas[1]
	elif(probabilidad_llegada[1] < rand_1 <= probabilidad_llegada[2]):
		llegadas_totales += numero_llegadas[2]
		llegadas += numero_llegadas[2]
	elif(probabilidad_llegada[2] < rand_1 <= probabilidad_llegada[3]):
		llegadas_totales += numero_llegadas[3]
		llegadas += numero_llegadas[3]
	elif(probabilidad_llegada[3] < rand_1 <= probabilidad_llegada[4]):
		llegadas_totales += numero_llegadas[4]
		llegadas += numero_llegadas[4]
	elif(probabilidad_llegada[4] < rand_1 <= probabilidad_llegada[5]):
		llegadas_totales += numero_llegadas[5]
		llegadas += numero_llegadas[5]
	# Barcazas atendidas
	atendidos = 0	
	if(rand_2 <=probabilidad_descarga[0]):
		atendidos_totales += numero_llegadas[0]
		atendidos = numero_llegadas[0]
	elif(probabilidad_descarga[0] < rand_2 <= probabilidad_descarga[1]):
		atendidos_totales += numero_llegadas[1]
		atendidos = numero_llegadas[1]
	elif(probabilidad_descarga[1] < rand_2 <= probabilidad_descarga[2]):
		atendidos_totales += numero_llegadas[2]
		atendidos = numero_llegadas[2]
	elif(probabilidad_descarga[2] < rand_2 <= probabilidad_descarga[3]):
		atendidos_totales += numero_llegadas[3]
		atendidos = numero_llegadas[3]
	elif(probabilidad_descarga[3] < rand_2 <= probabilidad_descarga[4]):
		atendidos_totales += numero_llegadas[4]
		atendidos = numero_llegadas[4]
	elif(probabilidad_descarga[4] < rand_2 <= probabilidad_descarga[5]):
		atendidos_totales += numero_llegadas[5]
		atendidos = numero_llegadas[5]
	
	if((llegadas - atendidos) > 0):
		restantes = llegadas - atendidos 
		retrasos_totales += 1

print("Número de retrasos:", retrasos_totales)
print("Atendidos promedio:", atendidos_totales / 15)
print("Llegadas promedio:", llegadas_totales / 15)
