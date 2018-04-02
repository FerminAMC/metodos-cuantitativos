import random

# a) Establezca una distribución de probabilidad y de probabilidad acumulada para la variable de las llegadas de los automóviles
distribucion_probabilidad = [.1, .15, .25, .3, .2]
distribucion_acumulada = [.1, .25, .5, .8, 1]
numero_autos = [4, 5, 6, 7, 8]
# c) Simule 15 horas de llegadas de automóviles y calcule el número promedio de llegadas por hora
total_autos = 0
for i in range(15):
	rand = random.random()
	if(rand <= distribucion_acumulada[0]):
		total_autos += numero_autos[0]
	elif(distribucion_acumulada[0] < rand <= distribucion_acumulada[1]):
		total_autos += numero_autos[1]
	elif(distribucion_acumulada[1] < rand <= distribucion_acumulada[2]):
		total_autos += numero_autos[2]
	elif(distribucion_acumulada[2] < rand <= distribucion_acumulada[3]):
		total_autos += numero_autos[3]
	elif(distribucion_acumulada[3] < rand <= distribucion_acumulada[4]):
		total_autos += numero_autos[4]
print("El número promedio de llegadas por hora es de:", total_autos / 15)

