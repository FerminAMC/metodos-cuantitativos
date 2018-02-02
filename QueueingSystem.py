time_between_arrivals = [20, 25, 30, 35, 40, 45, 50, 55, 60]
tba_probability = [0.2, 0.1, 0.22, 0.47, 0.67, 0.82, 0.92, 0.97, 1]

team_three = [20, 25, 30, 35, 40, 45, 50, 55, 60] # Time it takes a team unload a truck
team_three_probability = [0.05, 0.15, 0.35, 0.6, 0.72, 0.82, 0.9, 0.96, 1]

given_random_tba = [0.48355, 0.98977, 0.06533, 0.45128, 0.15486, 0.19241, 0.15997, 0.67940, 0.90872, 0.58997, 0.68691, 0.73488, 0.23423, 0.86675, 0.56856]
given_random_team = [0.83761, 0.14387, 0.51321, 0.72472, 0.05466, 0.84609, 0.29735, 0.59076, 0.76355, 0.29549, 0.61958, 0.17267, 0.10061, 0.45645, 0.86754, 0.35340]

number_of_days = 16

class Truck:
    def __init__(self, arrival_time, service_time, service_start):
        self.arrival_time = arrival_time
        self.service_time = service_time
        self.service_start = service_start
        self.service_stop = self.service_start + self.service_time
        self.wait = self.service_start - self.arrival_time

clock = 0
Trucks = []

for i in range(number_of_days):
    if(len(Trucks) == 0):
        for j in range(len(team_three_probability)):
            if(j == 0):
                if(given_random_team[i] <= team_three_probability[j]):
                    service_time = team_three[j]/60
            else:
                if(given_random_team[i] <= team_three_probability[j] and given_random_team[i] > team_three_probability[j-1]):
                    service_time = team_three[j]/60
        arrival_time = 0
        service_start = arrival_time
    else:
        for j in range(len(tba_probability)):
            if(j == 0):
                if(given_random_tba[i-1] <= tba_probability[j]):
                    tba_time = time_between_arrivals[j]/60
            else:
                if(given_random_tba[i-1] <= tba_probability[j] and given_random_tba[i-1] > tba_probability[j-1]):
                    tba_time = time_between_arrivals[j]/60
        for j in range(len(team_three_probability)):
            if(j == 0):
                if(given_random_team[i-1] <= team_three_probability[j]):
                    service_time = team_three[j]/60
            else:
                if(given_random_team[i-1] <= team_three_probability[j] and given_random_team[i-1] > team_three_probability[j-1]):
                    service_time = team_three[j]/60
        arrival_time += tba_time
        service_start = max(arrival_time, Trucks[-1].service_stop)

    Trucks.append(Truck(arrival_time, service_time, service_start))
    clock = arrival_time

print (clock)
