import datetime

from db import dbclub


def get_parties_tonight():
    result = list()
    for club in dbclub:
        party = get_party_tonight(club)
        if party is not None:
            result.append({
                "clubName": club["name"],
                "partyName": party
            })
    return result


def get_party_tonight(club):
    day = datetime.datetime.today().weekday()
    return club["parties"][day]

def get_party_by_index(index):
    return get_parties_tonight()[index]