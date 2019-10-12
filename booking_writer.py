# coding=utf-8
import json
import codecs

fileName = "dbbookings.json"


def flush_booking(booking):
    f = codecs.open(fileName, "a+", "utf-8")
    f.write(json.dumps(booking) + "\n")
    f.close()
