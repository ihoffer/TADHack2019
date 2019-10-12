from simwood_service import send_text
from db import dbclub, dbcont
import datetime

s1 = "Hi "
s2 = "The following parties are on tonight: \n"
s3 = "eFrancesco x"

ctr = 1
s = ''
day = datetime.datetime.today().weekday()

#message with the clubs that are available tonight
for j in dbclub:
    if dbclub[j][day] != "":
        s += str(ctr) + ". " + j + ": " + dbclub[j][day] + "\n"
        ctr += 1

#send out messages to contacts in directory
for i in dbcont:
    sf = s1 + i + ",\n\n" + s2 + s + "\n" + s3
    send_text(dbcont[i], sf)

