from flask import Flask, request
from flask_restful import Api, Resource

from simwood_service import send_text

app = Flask(__name__)
api = Api(app)

bookings_in_progress = dict()


class Handler(Resource):
    def post(self):
        json = request.get_json(force=True)

        self.handleResponse(json["data"]["originator"], json["data"]["message"])

        return "Message received, cheers", 200

    def handleResponse(self, originator, response):
        if originator not in bookings_in_progress:
            bookings_in_progress[originator] = BookingState(response)

        booking = bookings_in_progress[originator]
        booking.putResponse(response)

        new_question = booking.getNextQuestion()
        if new_question is not None:
            print "Sending {} to {}".format(new_question, originator)
            send_text(originator, new_question)
        else:
            print(booking.state)
            booking.flushBooking()


class BookingState:
    def __init__(self, club):
        self.currentQuestion = None
        self.missing = ["group_size"]
        self.state = {
            "club": int(club)
        }
        self.question = {
            "group_size": "What's your group size, m8?"
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

    def flushBooking(self):
        pass


api.add_resource(Handler, "/receive")

app.run(host='0.0.0.0', debug=False, port=80)