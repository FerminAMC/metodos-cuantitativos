random_arrival = [37, 77, 13, 10, 2, 18, 31, 19, 32, 85, 31, 94, 81, 43, 31, 58, 33, 51]
random_served = [37, 77, 13, 10, 2, 18, 31, 19, 32, 85, 31, 94, 81, 43, 31, 58, 33, 51]

day_arrival = 0
day_served = 0
cola = 0
retrasos = 0
capacidad = 0
numero_retrasos = 0
for i in range(15):
    # Llegadas
    if 0 < random_arrival[i] <= 13:
        day_arrival += 0
        cola += 0

    if 13 < random_arrival[i] <= 30:
        day_arrival += 1
        cola += 1

    if 30 < random_arrival[i] <= 45:
        day_arrival += 2
        cola += 2

    if 45 < random_arrival[i] <= 70:
        day_arrival += 3
        cola += 3

    if 70 < random_arrival[i] <= 90:
        day_arrival += 4
        cola += 4

    if 90 < random_arrival[i] <= 100:
        day_arrival += 5
        cola += 5

    # Atendidos
    if 0 < random_served[i] <= 5:
        capacidad = 1
        day_served += 1

    if 5 < random_served[i] <= 20:
        capacidad = 2
        day_served += 2

    if 20 < random_served[i] <= 70:
        capacidad = 3
        day_served += 3

    if 70 < random_served[i] <= 90:
        capacidad = 4
        day_served += 4

    if 90 < random_served[i] <= 100:
        capacidad = 5
        day_served += 5

    if capacidad < cola:
        numero_retrasos += 1
        retrasos += (cola - capacidad)
        cola = cola - capacidad

print("Llegadas promedio por día:", day_arrival/15)
print("Descargas promedio por día:", day_served/15)
print("Promedio de barcazas en cola", retrasos/numero_retrasos)
