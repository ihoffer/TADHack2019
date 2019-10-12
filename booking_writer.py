import json

fileName = "dbbookings.json"


def flush_booking(booking):
    f = open(fileName, "a+")
    f.write(json.dumps(booking))
    f.close()
