# coding=utf-8
import json
from simwood_service import send_text
from party_broker import get_parties_tonight
import datetime

data = []
with open('dbbookings.json', 'r') as f:
    for line in f:
        data.append(json.loads(line))
"""
with open('dbbookings.json', 'w') as f:
    del f
"""
day = datetime.datetime.today().weekday()
print("Sup Francesco, having a grand day? \nYou got some decisions to make fam.\n")

for i in data:
    s = i['name'] + " wants to go to " + i['clubName'] +" in a group of " + str(i['groupSize']) + "\n"
    print(s)
    print("Francescoed? [Y/N]")
    dec = str(raw_input()).capitalize()
    if dec == 'Y':
        send_text(i['phone'], "You're booked in for an amazing night in " + i['clubName'] + ". Prepare them moves!")
    else:
        ResponseN = ''
        remaining_parties = list(filter(lambda p : p['clubName'] != i['clubName'], get_parties_tonight()))
        print(remaining_parties)
        ctr = 1
        for j in remaining_parties:
                ResponseN += "{}. {}: {}\n".format(ctr, j["clubName"], j["partyName"])
                ctr += 1
        send_text(i['phone'], "We couldn't accomodate your request this time. Do you want to pick one of the other clubs? \n" + ResponseN)
