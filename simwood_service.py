# coding=utf-8
import requests

account_id = 931220
api_key = "2f4229c1a1bb38fcf87c58c461b08f173202b600"
url = "https://api.simwood.com/v3/"

user = "2f4229c1a1bb38fcf87c58c461b08f173202b600"
pw = "6c1f7c55c70acfecee16633175729fed2232c197"
app_name = "Test"

session = requests.Session()
session.auth = (user, pw)

def send_text(to, message):
    endpoint = url + "messaging/{}/sms".format(account_id)
    payload = {
        "from": app_name,
        "to": to,
        "message": message
    }
    print session.post(endpoint, json=payload)