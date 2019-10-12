# coding=utf-8
import datetime

from booking_writer import flush_booking
from message_broker import get_stage_confirmation

day = datetime.datetime.today().weekday()

from db import dbclub, dbcont

class BookingState:
    def __init__(self, originator, club):
        self.currentQuestion = "club"
        self.missing = ["groupSize"]
        self.state = {
            "club": int(club),
            "originator": originator
        }
        self.question = {
            "groupSize": "What's your group size, m8?"
        }

    def getNextQuestion(self):
        if len(self.missing) > 0:
            nextInfo = self.missing.pop()
            self.currentQuestion = nextInfo
            return self.question[nextInfo]
        return None

    def putResponse(self, response):
        if self.currentQuestion is not None:
            self.state[self.currentQuestion] = int(response)

    def getStageConfirmation(self):
        return get_stage_confirmation(self.currentQuestion)

    def flushBooking(self):
        payload = self.build_booking()
        flush_booking(payload)

    def build_booking(self):
        clubName = ""
        ctr = 0
        for j in dbclub:
            ctr += 1
            if dbclub[j][day] != "" and ctr == self.state["club"]:
                clubName = j
        name = dbcont[long(self.state["originator"])]
        payload = {
            "clubName": clubName,
            "name": name,
            "phone": self.state["originator"],
            "groupSize": self.state["groupSize"]
        }
        return payload