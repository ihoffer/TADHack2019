import json

mylist = [["Tonteria", "Matyi", 447887370010, 4],["Cuckoo", "Istvan", 447477468440, 8]]
bookings = {"bookings":mylist}

with open('dbbookings.json', 'w') as f:
  json.dump(bookings, f)