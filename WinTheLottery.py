#NOTE: to run this program, first cd into the folder where the program is contained
# Type chmod -x WinTheLottery.py in terminal
# Finally, type python WinTheLottery.py to run the script
import random

def win_lottery_fixed(placed_bet):
    right_numbers = [0, 0, 0, 0, 0]
    rand_list = []
    while(len(rand_list) < len(placed_bet)):
        rand_num = random.randint(1, 99)
        if(rand_num not in rand_list):
            rand_list.append(rand_num)
    for i in range(len(placed_bet)):
        if(placed_bet[i] == rand_list[i]):
            right_numbers[i] += 1
        else:
            break
    return right_numbers

def win_lottery_rand():
    right_numbers = [0, 0, 0, 0, 0]
    rand_list_1 = []
    rand_list_2 = []
    # Here I create the first random lottery numbers
    while(len(rand_list_1) < 5):
        rand_num = random.randint(1, 99)
        if(rand_num not in rand_list_1):
            rand_list_1.append(rand_num)
    # Here I create the second random lottery numbers
    while(len(rand_list_2) < 5):
        rand_num = random.randint(1, 99)
        if(rand_num not in rand_list_2):
            rand_list_2.append(rand_num)
    for i in range(len(right_numbers)):
        if(rand_list_1[i] == rand_list_2[i]):
            right_numbers[i] += 1
        else:
            break
    return right_numbers

number_of_tries = 90000
# Bet placed by the person
placed_bet = [3, 25, 28, 37, 71]
# Number of times a person gets the right number. Each position stands for first, second, third, fourth, and fifth numbers
winnings_fixed = [0, 0, 0, 0, 0]
winnings_random = [0, 0, 0, 0, 0]

for i in range(number_of_tries):
    res_1 = win_lottery_fixed(placed_bet)
    res_2 = win_lottery_rand()
    for j in range(5):
        winnings_fixed[j] += res_1[j]
        winnings_random[j] += res_2[j]

print "-- FIXED NUMBERS --"
print "With ", number_of_tries, " tries, the chances are:"
print "1 number: ", float(winnings_fixed[0])/number_of_tries
print "2 numbers: ", float(winnings_fixed[1])/number_of_tries
print "3 numbers: ", float(winnings_fixed[2])/number_of_tries
print "4 numbers: ", float(winnings_fixed[3])/number_of_tries
print "5 numbers: ", float(winnings_fixed[4])/number_of_tries
print "\n-- RANDOM NUMBERS --"
print "1 number: ", float(winnings_random[0])/number_of_tries
print "2 numbers: ", float(winnings_random[1])/number_of_tries
print "3 numbers: ", float(winnings_random[2])/number_of_tries
print "4 numbers: ", float(winnings_random[3])/number_of_tries
print "5 numbers: ", float(winnings_random[4])/number_of_tries
