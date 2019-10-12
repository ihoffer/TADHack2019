# coding=utf-8
from flask import Flask, request
from flask_restful import Api, Resource

from simwood_service import send_text

from BookingState import BookingState

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
            bookings_in_progress[originator] = BookingState(originator, response)

        booking = bookings_in_progress[originator]
        booking.putResponse(response)

        new_question = booking.getNextQuestion()
        if new_question is not None:
            print "Sending {} to {}".format(new_question, originator)
            send_text(originator, new_question)
        else:
            print(booking.state)
            booking.flushBooking()


api.add_resource(Handler, "/receive")
app.run(host='0.0.0.0', debug=False, port=80)