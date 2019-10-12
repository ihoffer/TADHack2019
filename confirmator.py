# coding=utf-8
import json
from simwood_service import send_text

data = []
with open('dbbookings.json', 'r') as f:
    for line in f:
        data.append(json.loads(line))

with open('dbbookings.json', 'w') as f:
    del f


print("Sup Francesco, having a grand day? \nYou got some decisions to make fam.\n")
for i in data:
    s = i['name'] + " wants to go to " + i['clubName'] +" in a group of " + str(i['groupSize']) + "\n"
    print(s)
    print("Francescoed? [Y/N]")
    dec = str(input())
    if dec == 'Y':
        send_text(i['phone'], "You're booked in fam. Prepare them moves!")
