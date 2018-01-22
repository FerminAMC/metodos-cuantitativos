import random
import math

def call_center(calls, call_answered, chance_woman, sale_woman, sale_man, cummulative_probability_woman, cummulative_probability_man, sale_level):
    comissions = 0
    success = int(calls * call_answered)
    woman = int((success * chance_woman) * sale_woman)
    man = int(abs(success * (chance_woman-1)) * sale_man)
    for i in range(woman):
        sale = random.random()
        for j in range(len(cummulative_probability_woman)):
            if j == 0:
                if(sale <= cummulative_probability_woman[j]):
                    comissions += 200*(j+1)
                    sale_level[j] += 1
            else:
                if ((sale > cummulative_probability_woman[j-1]) and (sale <= cummulative_probability_woman[j])):
                    comissions += 200*(j+1)
                    sale_level[j] += 1
    for k in range(man):
        sale = random.random()
        for l in range(len(cummulative_probability_man)):
            if l == 0:
                if(sale <= cummulative_probability_man[l]):
                    comissions += 200*(l+1)
                    sale_level[l] += 1
            else:
                if ((sale > cummulative_probability_man[l-1]) and (sale <= cummulative_probability_man[l])):
                    comissions += 200*(l+1)
                    sale_level[l] += 1
    z = 1.96
    n = calls
    x_m = float(comissions/(n))
    sum_x = 0
    for m in range(len(sale_level)):
        sum_x += math.pow(sale_level[m] - x_m, 2)
    s = math.sqrt(sum_x/(n-1))
    confidence_level_positive = x_m + (z*(s/math.sqrt(n)))
    confidence_level_negative = x_m - (z*(s/math.sqrt(n)))
    print ("Sales per categroy: ", sale_level)
    print ("Comissions: ", comissions)
    print ("Confidence level(+): ",  confidence_level_positive)
    print ("Confidence level(-): ", confidence_level_negative)

# Chance of person accepting the call
call_answered = .3
# Chance that a woman answers the call
chance_woman = .8
# Chance of concreting a sale per gender
sale_man = .25
sale_woman = .15
# Number of calls
calls = 5000
# Number of sales for each category
sale_level = [0, 0, 0, 0]
# Probabilities per gender
probability_woman = [0.6, 0.3, 0.1]
cummulative_probability_woman = [0.6, 0.9, 1]
probability_man = [0.1, 0.4, 0.3, 0.2]
cummulative_probability_man = [0.1, 0.5, 0.8, 1]

call_center(calls, call_answered, chance_woman, sale_woman, sale_man, cummulative_probability_woman, cummulative_probability_man, sale_level)
