import random
import math

def quizz_1(number_of_days, cars_per_day_probability, cars_per_day, small_car_probability, small_car, medium_car_probability, medium_car, big_car_probability, big_car):
    cash_needed = 0
    cash_per_day_stack = []
    for i in range(number_of_days):
        amount_of_cars = random.random()
        for j in range(len(cars_per_day_probability)):
            if j == 0:
                if amount_of_cars <= cars_per_day_probability[j]:
                    amount_of_cars = cars_per_day[j]
                    break
            else:
                if amount_of_cars > cars_per_day_probability[j-1] and amount_of_cars <= cars_per_day_probability[j]:
                    amount_of_cars = cars_per_day[j]
                    break
        for k in range(amount_of_cars):
            cash_per_day = 0
            for l in range(len(small_car)): # Doesn't matter what type of car you choose, they all have len = 5
                type_of_car = random.randint(1,3)
                type_of_job = random.random()
                if type_of_car == 1:
                    if l == 0:
                        if type_of_job <= small_car_probability[l]:
                            cash_needed += small_car[l]
                            cash_per_day += small_car[l]
                    else:
                        if type_of_job > small_car_probability[l-1] and type_of_job <= small_car_probability[l]:
                            cash_needed += small_car[l]
                            cash_per_day += small_car[l]
                if type_of_car == 2:
                    if l == 0:
                        if type_of_job <= medium_car_probability[l]:
                            cash_needed += medium_car[l]
                            cash_per_day += medium_car[l]
                    else:
                        if type_of_job > medium_car_probability[l-1] and type_of_job <= medium_car_probability[l]:
                            cash_needed += medium_car[l]
                            cash_per_day += medium_car[l]
                if type_of_car == 3:
                    if l == 0:
                        if type_of_job <= big_car_probability[l]:
                            cash_needed += big_car[l]
                            cash_per_day += big_car[l]
                    else:
                        if type_of_job > big_car_probability[l-1] and type_of_job <= big_car_probability[l]:
                            cash_needed += big_car[l]
                            cash_per_day += big_car[l]
            cash_per_day_stack.append(cash_per_day)

    average_cash = cash_needed/number_of_days
    z = [1.15034938, 1.281551566, 1.439531471, 1.644853627, 1.959963985]
    asked_probability = [75, 80, 85, 90, 95]
    for m in range(len(z)):
        r = 0
        sum_x = 0
        for n in range(number_of_days):
                x = cash_per_day_stack.pop()
                sum_x += math.pow(x - average_cash, 2)
        r = math.sqrt(sum_x / number_of_days)
        print ("Average cash needed to buy ", asked_probability[m], " percent of car parts: ", average_cash + z[m] * (r / math.sqrt(number_of_days)))
        print ("Average cash needed to buy ", asked_probability[m], " percent of car parts: ", average_cash - z[m] * (r / math.sqrt(number_of_days)))



cars_per_day_probability = [0.05, 0.2, 0.5, 0.75, 0.9, 1]
cars_per_day = [3, 4, 5, 6, 7, 8]

small_car_probability = [0.45, 0.6, 0.8, 0.9, 1]
small_car = [350, 1575, 1925, 2540, 700]

medium_car_probability = [0.25, 0.5, 0.65, 0.85, 1]
medium_car = [550, 1975, 2545, 2925, 700]

big_car_probability = [0.1, 0.25, 0.55, 0.95, 1]
big_car = [750, 2275, 2845, 3415, 700]

number_of_days = 5000


quizz_1(number_of_days, cars_per_day_probability, cars_per_day, small_car_probability, small_car, medium_car_probability, medium_car, big_car_probability, big_car)
z = [1.15034938, 1.281551566, 1.439531471, 1.644853627, 1.959963985]
