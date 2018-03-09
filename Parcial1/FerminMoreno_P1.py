import random

daily_demand = [0, 1, 2, 3, 4, 5, 6, 7, 8]
daily_demand_probability = [0.04, 0.1, 0.2, 0.4, 0.7, 0.88, 0.96, 0.99, 1]

delivery_time = [1, 2, 3, 4]
delivery_time_probability = [0.25, 0.75, 0.95, 1]

runs = 200

inventory = 0
min_inventory = 5
order_quantity = 15
order_cost = 50
inventory_cost = 26 #price per unit remaining at the end of the year
missing_cost = 25 #price per unit for missing item
ItemOrders = []
total_orders = 0
total_missing_cost = 0

class ItemOrder:
    def __init__(self, arrival_time, ordered_units):
        self.arrival_time = arrival_time
        self.ordered_units = ordered_units

for i in range(runs):
    demand = 0
    arrival_time = 0

    for j in range(len(ItemOrders)):
        ItemOrders[j].arrival_time -= 1
        if(ItemOrders[j].arrival_time == 0):
            inventory += ItemOrders[j].ordered_units

    for j in range(len(daily_demand_probability)):
        random_num = random.random()
        if j == 0:
            if(random_num <= daily_demand_probability[j]):
                demand = daily_demand[j]
                inventory -= demand
        else:
            if(random_num <= daily_demand_probability[j] and random_num > daily_demand_probability[j-1]):
                demand = daily_demand[j]
                inventory -= demand

    if(inventory <= min_inventory):
        for j in range(len(delivery_time_probability)):
            random_num = random.random()
            if j == 0:
                if(random_num <= delivery_time_probability[j]):
                    arrival_time = delivery_time[j]
            else:
                if(random_num <= delivery_time_probability[j] and random_num > delivery_time_probability[j-1]):
                    arrival_time = delivery_time[j]

        ItemOrders.append(ItemOrder(arrival_time, 15))
        total_orders += 1
    if(inventory < 0):
        total_missing_cost += missing_cost * abs(inventory)

print("Cost for not having enough inventory: ", total_missing_cost)
print("Cost for ordering every time the inventory is <= 5: ", total_orders*order_cost)
if(inventory > 0):
    print("Cost for having extra inventory at the end of the year: ", inventory*inventory_cost)
else:
    print("Cost for having extra inventory at the end of the year: 0")
