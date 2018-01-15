import random

def buy_tortas(cumulative_probability, gains_per_amount):
    demanded = random.randint(1, 6)   # This represents how many tortas where ordered for the day
    sold = random.random()  # This represents the chance of selling a certain amount of tortas
    for i in range(len(probability)):
        if (i == 0):
            if sold <= probability[i]:
                if (demanded > i+1):
                    gains_per_amount[demanded-1] += 12*((7*(i+1)) + (((demanded-i+1)/2)*1.5) - (3*demanded))
                if (demanded == i+1):
                    gains_per_amount[demanded-1] += 12*((4*i+1))
        else:
            if (sold <= cumulative_probability[i] and sold > cumulative_probability[i-1]):
                if (demanded > i+1):
                    gains_per_amount[demanded-1] += 12*((7*(i+1)) + (((demanded-i+1)/2)*1.5) - (3*demanded))
                if (demanded == i+1):
                    gains_per_amount[demanded-1] += 12*((4*i+1))
                else:
                    gains_per_amount[demanded-1] += 12*((7*(i+1)) + (((demanded-i+1)/2)*1.5) - (3*demanded) - (5*(i+1-demanded)))

gains_per_amount = [0, 0, 0, 0, 0, 0]
number_of_days = 5000
probability = [0.05, 0.1, 0.2, 0.4, 0.2, 0.05]
cumulative_probability = [0.05, 0.15, 0.35, 0.75, 0.95, 1]

#NOTE: Price of a torta: $16
#NOTE: Cost of making a torta: $9
#NOTE: Cost of bread: $3

for i in range(number_of_days):
    buy_tortas(cumulative_probability, gains_per_amount)
print gains_per_amount
