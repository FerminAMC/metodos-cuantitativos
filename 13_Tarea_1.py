import numpy as np
import random

class Client:
    def __init__(self, arrival_time, service_start):
        self.arrival_time = arrival_time
        self.service_time = np.random.uniform(0, 1)
        self.service_start = service_start
        self.service_stop = self.service_start + self.service_time
        self.wait = self.service_start - self.arrival_time

runs = 10 # in this case, runs represents the number of hours
lambda_clients = 40
Clients = []
time = 0

number_of_clients = np.random.poisson(lambda_clients)
for i in range(number_of_clients):
    if(len(Clients_list) == 0):
        arrival_time = random.random()
        service_start = arrival_time
    else:
        service_start = max(arrival_time, Clients[-1].service_stop)
    Clients.append(Client(arrival_time, service_start))
