import random

time_between_arrivals = [20, 25, 30, 35, 40, 45, 50, 55, 60]
tba_probability = [0.2, 0.1, 0.22, 0.47, 0.67, 0.82, 0.92, 0.97, 1]

team_three = [20, 25, 30, 35, 40, 45, 50, 55, 60] # Time it takes a team unload a truck
team_three_probability = [0.05, 0.15, 0.35, 0.6, 0.72, 0.82, 0.9, 0.96, 1]

given_random_tba = [0.48355, 0.98977, 0.06533, 0.45128, 0.15486, 0.19241, 0.15997, 0.67940, 0.90872, 0.58997, 0.68691, 0.73488, 0.23423, 0.86675, 0.56856]
given_random_team = [0.83761, 0.14387, 0.51321, 0.72472, 0.05466, 0.84609, 0.29735, 0.59076, 0.76355, 0.29549, 0.61958, 0.17267, 0.10061, 0.45645, 0.86754, 0.35340]

number_of_days = 16

resp_array = ["Lost Time", "Truck Waiting Time", "Queue Length"]

truck_queue = []

for i in range(number_of_days):
    arrival_time = 0
    worked_time = 0
    resp_array.append("Day: " + str(i)) # Adds the Day to the list
    if(i == 0):
        resp_array.append("Random Arrival Time: -") # Adds the Random Arrival Time to the list
        resp_array.append("Time Between Arrivals: 0")
        for j in range(len(team_three_probability)):
            if(j == 0):
                if(given_random_team[i] <= team_three_probability[j]):
                    team_time = team_three[j]/60
            else:
                if(given_random_team[i] <= team_three_probability[j] and given_random_team[i] > team_three_probability[j-1]):
                    team_time = team_three[j]/60
        truck_queue.append([arrival_time, team_time])
        resp_array.append("Arrival Time: " + str(arrival_time))
        resp_array.append("Service Start: " + str(arrival_time))
        resp_array.append("Random Servie Duration: " + str(given_random_team[i]))
        truck_info = truck_queue.pop(0)
        worked_time += truck_info[1] + team_time
        resp_array.append("Service Stop: " + str(worked_time))
        resp_array.append("Lost Time: 0")
        resp_array.append("Truck Waiting Time: 0")
        resp_array.append("Queue Length: " + str(len(truck_queue)))
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
                    team_time = team_three[j]/60
            else:
                if(given_random_team[i-1] <= team_three_probability[j] and given_random_team[i-1] > team_three_probability[j-1]):
                    team_time = team_three[j]/60
        arrival_time +=  tba_time
        truck_queue.append([arrival_time, team_time])
        if(len(truck_queue) == 1):
            service_start = arrival_time
            service_stop = arrival_time + team_time


print (resp_array)
