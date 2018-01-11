import random

def random_numbers_commerce(n, chance):
    positive_rounding = 0 # By positive rounding I mean that it "benefits" the client
    negative_rounding = 0 # By negative rounding I mean that it "affects" the client
    for i in range(n):
        x = random.random()
        if(x >= chance):
            positive_rounding += 1
        else:
            negative_rounding += 1
    return (positive_rounding, negative_rounding)
# Number of times the program will try the Random Numbers Comerce
number_of_tries = 50000
# Chance for positive rounding for the client
chance = 0.2
# Extra cents of the object to be purchased
extra_cents = .47
resp = random_numbers_commerce(number_of_tries, chance)
print "Positive rounding: ", resp[0]
print "Negative rounding: ", resp[1]
print "Assuming the product has ", extra_cents, " extra cents"
if(resp[0] > resp[1]):
    print "The store has to pay: ", resp[0]*1
    print "The store saves: ", resp[1]*1
else:
    print "The client has to pay: ", resp[1]*1
    print "The client saves", resp[0]*1
