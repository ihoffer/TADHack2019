# coding=utf-8
import json
import codecs

fileName = "dbbookings.json"
auditFile = "audit.csv"


def flush_booking(booking):
    f = codecs.open(fileName, "a+", "utf-8")
    f.write(json.dumps(booking) + "\n")
    f.close()


def flush_complete_booking(booking):
    f = codecs.open(auditFile, "a+", "utf-8")
    f.write(booking + "\n")
    f.close()
