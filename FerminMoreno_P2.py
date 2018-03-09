
arrival_time = [1, 2, 3, 4, 5]
arrival_time_probability = [0.2, 0.45, 0.75, 0.9, 1]
service_time = [1, 2, 3, 4, 5, 6]
service_time_probability = [0.1, 0.25, 0.6, 0.75, 0.9, 1]

random_arrival = [0.52, 0.37, 0.82, 0.69, 0.98, 0.96, 0.33, 0.5, 0.88, 0.90, 0.5, 0.27, 0.45, 0.81, 0.66, 0.74, 0.3, 0.59, 0.67, 0.28, 0.02, 0.74, 0.35, 0.24, 0.03, 0.29, 0.6, 0.74, 0.85, 0.9]
random_service = [0.6, 0.6, 0.8, 0.53, 0.69, 0.37, 0.06, 0.63, 0.57, 0.02, 0.94, 0.52, 0.69, 0.33, 0.32, 0.30, 0.48, 0.88, 0.33, 0.48, 0.72, 0.33, 0.62, 0.13, 0.74, 0.68, 0.22, 0.44, 0.42, 0.09]

class Client:
    def __init__(self, arrival_time, service_time, service_start):
        self.arrival_time = arrival_time
        self.service_time = service_time
        self.service_start = service_start
        self.service_stop = self.service_start + self.service_time
        self.wait = self.service_start - self.arrival_time

#NOTE: I consider that a client is not served if the clock reaches the limit, even if he arrived on time

# Excercise a
clock = 0
Clients = []
arrival_time_client = 0
i = 0
while(clock < 60):
    if(len(Clients) == 0):
        for j in range(len(service_time_probability)):
            if(j == 0):
                if(random_service[i] <= service_time_probability[j]):
                    service_time_client = service_time[j]
            else:
                if(random_service[i]<= service_time_probability[j] and random_service[i]>service_time_probability[j-1]):
                    service_time_client = service_time[j]
        service_start = arrival_time_client
    else:
        for j in range(len(service_time_probability)):
            if(j == 0):
                if(random_service[i] <= service_time_probability[j]):
                    service_time_client = service_time[j]
            else:
                if(random_service[i]<= service_time_probability[j] and random_service[i]>service_time_probability[j-1]):
                    service_time_client = service_time[j]
        for j in range(len(arrival_time_probability)):
            if(j == 0):
                if(random_arrival[i] <= arrival_time_probability[j]):
                    tba_client = arrival_time[j]
            else:
                if(random_arrival[i]<= arrival_time_probability[j] and random_arrival[i]>arrival_time_probability[j-1]):
                    tba_client = arrival_time[j]
        arrival_time_client += tba_client
        service_start = max(arrival_time_client, Clients[-1].service_stop)

    Clients.append(Client(arrival_time_client, service_time_client, service_start))
    clock = service_start
    i += 1
    if(i > 29):
        i = 0

total_wait = 0
clients_waited = 0
for i in range(len(Clients)):
    if(Clients[i].wait > 0):
        total_wait += Clients[i].wait
        clients_waited += 1

print("Cost of waiting time for exercise a:", total_wait)

# Exercise c (this simulation is run with only one window operating)
total_wait = 0
clients_waited = 0
i = 0
for k in range(200):
    clock = 0
    Clients = []
    arrival_time_client = 0
    while(clock < 420):
        if(len(Clients) == 0):
            for j in range(len(service_time_probability)):
                if(j == 0):
                    if(random_service[i] <= service_time_probability[j]):
                        service_time_client = service_time[j]
                else:
                    if(random_service[i]<= service_time_probability[j] and random_service[i]>service_time_probability[j-1]):
                        service_time_client = service_time[j]
            service_start = arrival_time_client
        else:
            for j in range(len(service_time_probability)):
                if(j == 0):
                    if(random_service[i] <= service_time_probability[j]):
                        service_time_client = service_time[j]
                else:
                    if(random_service[i]<= service_time_probability[j] and random_service[i]>service_time_probability[j-1]):
                        service_time_client = service_time[j]
            for j in range(len(arrival_time_probability)):
                if(j == 0):
                    if(random_arrival[i] <= arrival_time_probability[j]):
                        tba_client = arrival_time[j]
                else:
                    if(random_arrival[i]<= arrival_time_probability[j] and random_arrival[i]>arrival_time_probability[j-1]):
                        tba_client = arrival_time[j]
            arrival_time_client += tba_client
            service_start = max(arrival_time_client, Clients[-1].service_stop)

        Clients.append(Client(arrival_time_client, service_time_client, service_start))
        clock = service_start
        i += 1
        if(i > 29):
            i = 0

    for l in range(len(Clients)):
        if(Clients[l].wait > 0):
            total_wait += Clients[l].wait
            clients_waited += 1

print("Cost of waiting time for exercise c:", total_wait)
