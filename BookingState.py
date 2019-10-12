# coding=utf-8
from booking_writer import flush_booking
from message_broker import get_stage_confirmation, get_stage_question
from party_broker import get_party_by_index

from db import dbcont


class BookingState:
    def __init__(self, originator, club):
        self.currentQuestion = "club"
        self.missing = ["groupSize"]
        self.state = {
            "club": int(club),
            "originator": originator
        }

    def getNextQuestion(self):
        if len(self.missing) > 0:
            nextInfo = self.missing.pop()
            self.currentQuestion = nextInfo
            return get_stage_question(nextInfo)
        return None

    def putResponse(self, response):
        if self.currentQuestion is not None:
            self.state[self.currentQuestion] = int(response)

    def getStageConfirmation(self):
        return get_stage_confirmation(self.currentQuestion)

    def getNextMessage(self):
        confirmation = self.getStageConfirmation()
        question = self.getNextQuestion()
        message = ""
        if confirmation is not None:
            message += confirmation + " "
        if question is not None:
            message += question
        return message if message != "" else None

    def flushBooking(self):
        payload = self.build_booking()
        flush_booking(payload)

    def build_booking(self):
        club_name = get_party_by_index(self.state["club"])["clubName"]
        name = dbcont[long(self.state["originator"])]
        payload = {
            "clubName": club_name,
            "name": name,
            "phone": self.state["originator"],
            "groupSize": self.state["groupSize"]
        }
        return payload
