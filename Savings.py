import random

transportation_expenses = [1300, 1800, 2300, 2800, 3300, 3800]
transportation_expenses_probability = [.16, .33, .5, .66, .83, 1]

number_of_runs = 5000
saved_money = 0
transportation_money = 0
food_money = 0
fun_money = 0
invested_money = 0

for i in range(number_of_runs):
    money = 3000
    random_num = random.random()
    for j in range(len(transportation_expenses_probability)):
        if j == 0:
            if(random_num <= transportation_expenses_probability[j]):
                transportation_money += transportation_expenses[j]
                money -= transportation_expenses[j]
        else:
            if(random_num <= transportation_expenses_probability[j] and random_num > transportation_expenses_probability[j-1]):
                transportation_money += transportation_expenses[j]
                money -= transportation_expenses[j]
    if(money <= 0):
        food_money += 100
        saved_money += money - 200
    else:
        food_money += (money * .4)
        money = (money * .6)
        fun_money += (money * .05)
        money = (money * .95)
        invested_money += (money * .1)
        money = (money * .9)
        saved_money += money

print ("Money earned before expenses:", 3000 * number_of_runs)
print ("Money left after expenses: ", saved_money)
print ("Average money left after expenses: ", saved_money/number_of_runs)
print ("Money invested: ", invested_money)
print ("Average money invested: ", invested_money/number_of_runs)
print ("Money spent on transportation: ", transportation_money)
print ("Average money spent on transportation: ", transportation_money/number_of_runs)
print ("Money spent on food: ", food_money)
print ("Average money spent on food: ", food_money/number_of_runs)
print ("Money spent on fun: ", fun_money)
print ("Average money spent on fun: ", fun_money/number_of_runs)
