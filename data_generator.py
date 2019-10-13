import numpy as np
import random

names = ["Matyas", "Istvan", "Mike", "Clara", "Anna", "Alice", "Jake", "Sally", "Karen", "Kyle"]
names_p = [1, 2, 3, 4, 6, 8, 1, 9, 10, 11]
names_p_sum = sum(names_p)
names_p = list(map(lambda x: float(x) / names_p_sum, names_p))

clubs = ["Tonteria", "Cuckoo", "Toyroom", "Cafe de Paris", "Circe le Soir"]

days = range(1, 15)
days_p = [3, 5, 2, 1, 7, 8, 2, 4, 6, 3, 3, 8, 10, 5]
days_p_sum = sum(days_p)
days_p = list(map(lambda x: float(x) / days_p_sum, days_p))

decisions = [True, False]

for _ in range(250):
    day = np.random.choice(days, p=days_p)
    selected_name = np.random.choice(names, p=names_p)
    phone_number = "44123456789"
    club_name = ""
    if day < 8:
        clubs_p = [0.4, 0.15, 0.1, 0.1, 0.25]
        club_name = np.random.choice(clubs, p=clubs_p)
    else:
        clubs_p = [0.1, 0.15, 0.1, 0.5, 0.15]
        club_name = np.random.choice(clubs, p=clubs_p)
    party_size = random.randint(3, 12)
    decision = False
    if party_size > 5:
        decisions_p = [0.3, 0.7]
        decision = np.random.choice(decisions, p=decisions_p)
    else:
        decision = np.random.choice(decisions)
    line = "2019-10-{},{},{},{},{},{}".format(day, selected_name, phone_number, club_name, party_size, decision)
    print(line)
