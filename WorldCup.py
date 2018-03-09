import random

# Team scores where taken from the official FIFA website.
# The first element in the array is the team name, the second is the
# team score, and the third is the number of times they win in the simulation
teams = [["Brazil", 227, 0], ["Germany", 218, 0],
["Argentina", 140, 0], ["Spain", 99, 0], ["England", 98, 0],
["France", 96, 0], ["Uruguay", 72, 0], ["Sweden", 61, 0],
["Russia", 59, 0], ["Serbia", 59, 0], ["Mexico", 56, 0],
["Belgium", 54, 0],["Poland", 50, 0], ["Portugal", 43, 0],
["Switzerland", 39, 0], ["Denmark", 26, 0], ["Korea Republic", 24, 0],
["Croatia", 23, 0], ["Colombia", 23, 0], ["Costa Rica", 19, 0],
["Nigeria", 18, 0], ["Japan", 16, 0], ["Peru", 15, 0], ["Morocco", 10, 0],
["Australia", 9, 0], ["Senegal", 8, 0], ["Saudi Arabia", 8, 0],
["Tunisia", 7, 0], ["Iran", 6, 0], ["Egypt", 2, 0], ["Iceland", 1, 0],
["Panama", 1, 0]]

winners = []
runs = 5000
for j in range(runs):
    # This array will be populated with the winners of first round
    round_1_winners = []

    # First round of games 32 teams, 16 games
    #print("First round of games:")
    for i in range(16):
        # Pick team 1 from array and remove it
        random_num1 = random.randint(0, len(teams)-1)
        team1 = teams[random_num1]
        teams.pop(random_num1)
        # Pick team 2 from array and remove it
        random_num2 = random.randint(0, len(teams)-1)
        team2 = teams[random_num2]
        teams.pop(random_num2)

        #print(team1[0], "vs", team2[0])

        chance_team1 = team1[1] / (team1[1] + team2[1])
        if(chance_team1 < random.random() <= 1):
            # I increase the team points when they win. Small teams get a huge
            # bump of points when they beat a big team (rarely happens), and
            # big teams increase very little when they beat small teams. Similar
            # to what happens when a team is on a winning streak.
            team2[1] += team1[1]/3
            round_1_winners.append(team2)
        else:
            team1[1] += team2[1]/3
            round_1_winners.append(team1)
        #print("Winner:", round_1_winners[i][0], "\n")


    # This array will be populated with the winners of second round
    round_2_winners = []

    # Second round of games 16 teams, 8 games
    #print("Second round of games:")
    for i in range(8):
        # Pick team 1 from array and remove it
        random_num1 = random.randint(0, len(round_1_winners)-1)
        team1 = round_1_winners[random_num1]
        round_1_winners.pop(random_num1)
        # Pick team 2 from array and remove it
        random_num2 = random.randint(0, len(round_1_winners)-1)
        team2 = round_1_winners[random_num2]
        round_1_winners.pop(random_num2)

        #print(team1[0], "vs", team2[0])

        chance_team1 = team1[1] / (team1[1] + team2[1])
        if(chance_team1 < random.random() <= 1):
            team2[1] += team1[1]/3
            round_2_winners.append(team2)
        else:
            team1[1] += team2[1]/3
            round_2_winners.append(team1)
        #print("Winner:", round_2_winners[i][0], "\n")


    # This array will be populated with the winners of third round
    round_3_winners = []

    # Third round of games 8 teams, 4 games
    #print("Third round of games:")
    for i in range(4):
        # Pick team 1 from array and remove it
        random_num1 = random.randint(0, len(round_2_winners)-1)
        team1 = round_2_winners[random_num1]
        round_2_winners.pop(random_num1)
        # Pick team 2 from array and remove it
        random_num2 = random.randint(0, len(round_2_winners)-1)
        team2 = round_2_winners[random_num2]
        round_2_winners.pop(random_num2)

        #print(team1[0], "vs", team2[0])

        chance_team1 = team1[1] / (team1[1] + team2[1])
        if(chance_team1 < random.random() <= 1):
            team2[1] += team1[1]/3
            round_3_winners.append(team2)
        else:
            team1[1] += team2[1]/3
            round_3_winners.append(team1)
        #print("Winner:", round_3_winners[i][0], "\n")


    # This array will be populated with the winners of fourth round
    round_4_winners = []

    # Third round of games 4 teams, 2 games
    #print("Third round of games:")
    for i in range(2):
        # Pick team 1 from array and remove it
        random_num1 = random.randint(0, len(round_3_winners)-1)
        team1 = round_3_winners[random_num1]
        round_3_winners.pop(random_num1)
        # Pick team 2 from array and remove it
        random_num2 = random.randint(0, len(round_3_winners)-1)
        team2 = round_3_winners[random_num2]
        round_3_winners.pop(random_num2)

        #print(team1[0], "vs", team2[0])

        chance_team1 = team1[1] / (team1[1] + team2[1])
        if(chance_team1 < random.random() <= 1):
            team2[1] += team1[1]/3
            round_4_winners.append(team2)
        else:
            team1[1] += team2[1]/3
            round_4_winners.append(team1)
        #print("Winner:", round_4_winners[i][0], "\n")

    # Fianl game. This is it for the two remaining teams!
    #print(round_4_winners[0][0], "vs", round_4_winners[1][0])
    chance_team1 = round_4_winners[0][1] / (round_4_winners[0][1] + round_4_winners[1][1])
    if(chance_team1 < random.random() <= 1):
        winner = round_4_winners[1]
    else:
        winner = round_4_winners[0]


    aux = 1
    if(len(winners) > 0):
        aux = 0
        for k in range(len(winners)):
            if(winner[0] == winners[k][0]):
                winners[k][2] += 1
                aux = 1
    else:
        winner[2] += 1
        winners.append(winner)

    if(aux == 0):
        winner[2] += 1
        winners.append(winner)

    teams = [["Brazil", 227, 0], ["Germany", 218, 0],
    ["Argentina", 140, 0], ["Spain", 99, 0], ["England", 98, 0],
    ["France", 96, 0], ["Uruguay", 72, 0], ["Sweden", 61, 0],
    ["Russia", 59, 0], ["Serbia", 59, 0], ["Mexico", 56, 0],
    ["Belgium", 54, 0],["Poland", 50, 0], ["Portugal", 43, 0],
    ["Switzerland", 39, 0], ["Denmark", 26, 0], ["Korea Republic", 24, 0],
    ["Croatia", 23, 0], ["Colombia", 23, 0], ["Costa Rica", 19, 0],
    ["Nigeria", 18, 0], ["Japan", 16, 0], ["Peru", 15, 0], ["Morocco", 10, 0],
    ["Australia", 9, 0], ["Senegal", 8, 0], ["Saudi Arabia", 8, 0],
    ["Tunisia", 7, 0], ["Iran", 6, 0], ["Egypt", 2, 0], ["Iceland", 1, 0],
    ["Panama", 1, 0]]


best_team = ["", 0, 0]
for i in range(len(winners)):
    #print(winners[i])
    if(best_team[2] < winners[i][2]):
        best_team = winners[i]

# Overall, Brazil seems to be the best team, being closely followed by Germany
# For this simulation I based myself solely on the teams score. In order to do
# this simulation properly more data has to be considered
print("El mejor equipo fue:", best_team[0])
print("Número de victorias:", best_team[2])
print("Porcentaje de victorias", (best_team[2]/runs)*100,"%")
