# coding=utf-8
import datetime

from simwood_service import send_text
from db import dbcont
from party_broker import get_parties_tonight

s1 = "Hi "
s2 = "The following parties are on tonight: \n"
s3 = "eFrancesco x"

ctr = 1
s = ''
day = datetime.datetime.today().weekday()

#message with the clubs that are available tonight
partiesTonight = get_parties_tonight()
for party in partiesTonight:
    s += "{}. {}: {}\n".format(ctr, party["clubName"], party["partyName"])
    ctr += 1

#send out messages to contacts in directory
for i in dbcont:
    sf = s1 + dbcont[i] + ",\n\n" + s2 + s + "\n" + s3
    send_text(i, sf)

